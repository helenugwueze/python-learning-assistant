from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from pathlib import Path
import sqlite3, json, contextlib, io, importlib.util

BASE = Path(__file__).resolve().parent
DB = BASE / 'learning_assistant.db'
DATA = BASE / 'data'
app = Flask(__name__)
app.secret_key = 'change-this-to-a-long-random-secret-before-deployment'

LESSON_TITLES = {
 1:'Introduction to Python',2:'Variables',3:'Data Types',4:'Strings',5:'Numbers',
 6:'Type Conversion',7:'Operators',8:'User Input',9:'Output',10:'Comments',
 11:'Conditional Statements',12:'Comparison Operators',13:'Logical Operators',
 14:'For Loops',15:'While Loops',16:'Break and Continue',17:'Nested Loops',
 18:'Lists',19:'Tuples',20:'Sets',21:'Dictionaries',22:'Functions',23:'List Comprehensions'
}

def connect():
    con=sqlite3.connect(DB); con.row_factory=sqlite3.Row; return con

def init_db():
    with connect() as con:
        con.execute('''CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL, password TEXT NOT NULL)''')
        con.execute('''CREATE TABLE IF NOT EXISTS completed(user_id INTEGER NOT NULL, lesson INTEGER NOT NULL, PRIMARY KEY(user_id, lesson))''')
        con.execute('''CREATE TABLE IF NOT EXISTS quiz_results(id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL, score INTEGER NOT NULL, total INTEGER NOT NULL, created_at TEXT DEFAULT CURRENT_TIMESTAMP)''')

def current_user(): return session.get('user_id')

def login_required(fn):
    from functools import wraps
    @wraps(fn)
    def wrapper(*args,**kwargs):
        if not current_user(): return redirect(url_for('login'))
        return fn(*args,**kwargs)
    return wrapper

@app.context_processor
def common(): return {'username':session.get('username')}

@app.route('/')
def home(): return redirect(url_for('dashboard')) if current_user() else redirect(url_for('login'))

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method=='POST':
        username=request.form.get('username','').strip(); password=request.form.get('password','')
        if not username or len(password)<8:
            flash('Enter a username and a password with at least 8 characters.','error')
        else:
            try:
                with connect() as con:
                    con.execute('INSERT INTO users(username,password) VALUES(?,?)',(username,generate_password_hash(password)))
                flash('Account created. Please sign in.','success'); return redirect(url_for('login'))
            except sqlite3.IntegrityError: flash('That username is already in use.','error')
    return render_template('auth.html', mode='register')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form.get('username','').strip(); password=request.form.get('password','')
        with connect() as con: user=con.execute('SELECT * FROM users WHERE username=?',(username,)).fetchone()
        if user and check_password_hash(user['password'],password):
            session.clear(); session['user_id']=user['id']; session['username']=user['username']; return redirect(url_for('dashboard'))
        flash('Incorrect username or password.','error')
    return render_template('auth.html', mode='login')

@app.route('/logout')
def logout(): session.clear(); return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    uid=current_user()
    with connect() as con:
        done=con.execute('SELECT COUNT(*) n FROM completed WHERE user_id=?',(uid,)).fetchone()['n']
        result=con.execute('SELECT score,total,created_at FROM quiz_results WHERE user_id=? ORDER BY id DESC LIMIT 1',(uid,)).fetchone()
    return render_template('dashboard.html', total=23, done=done, percent=round(done/23*100), last_result=result)

@app.route('/lessons')
@login_required
def lessons():
    uid=current_user()
    with connect() as con: done={r['lesson'] for r in con.execute('SELECT lesson FROM completed WHERE user_id=?',(uid,))}
    return render_template('lessons.html', lessons=LESSON_TITLES, done=done)

def lesson_text(number):
    if number <= 10:
        lessons_path = DATA / 'lessons_1_10.json'
        lessons = json.loads(lessons_path.read_text(encoding='utf-8'))
        return lessons.get(str(number), 'This lesson could not be found.')
    path=DATA/f'lesson_{number}.py'
    if not path.exists(): return 'The lesson file was not found in the uploaded project.'
    spec=importlib.util.spec_from_file_location(f'lesson_{number}',path); module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    output=io.StringIO()
    with contextlib.redirect_stdout(output): getattr(module,f'display_lesson_{number}')()
    return output.getvalue()

@app.route('/lessons/<int:number>')
@login_required
def lesson(number):
    if number not in LESSON_TITLES: return redirect(url_for('lessons'))
    with connect() as con: done=con.execute('SELECT 1 FROM completed WHERE user_id=? AND lesson=?',(current_user(),number)).fetchone()
    return render_template('lesson.html', number=number, title=LESSON_TITLES[number], content=lesson_text(number), done=bool(done))

@app.post('/lessons/<int:number>/complete')
@login_required
def complete_lesson(number):
    if number in LESSON_TITLES:
        with connect() as con: con.execute('INSERT OR IGNORE INTO completed(user_id,lesson) VALUES(?,?)',(current_user(),number))
        flash(f'Lesson {number} marked as completed.','success')
    return redirect(url_for('lesson',number=number))

@app.route('/quiz', methods=['GET','POST'])
@login_required
def quiz():
    questions=json.loads((DATA/'questions.json').read_text())
    if request.method=='POST':
        score=sum(1 for i,q in enumerate(questions) if request.form.get(f'q{i}')==q['answer'])
        with connect() as con: con.execute('INSERT INTO quiz_results(user_id,score,total) VALUES(?,?,?)',(current_user(),score,len(questions)))
        return render_template('quiz_result.html',score=score,total=len(questions))
    return render_template('quiz.html',questions=questions)

@app.route('/progress')
@login_required
def progress():
    uid=current_user()
    with connect() as con:
        done=con.execute('SELECT lesson FROM completed WHERE user_id=? ORDER BY lesson',(uid,)).fetchall()
        results=con.execute('SELECT score,total,created_at FROM quiz_results WHERE user_id=? ORDER BY id DESC LIMIT 5',(uid,)).fetchall()
    return render_template('progress.html',done=[r['lesson'] for r in done],total=23,results=results)

if __name__=='__main__':
    init_db(); app.run(debug=True)
