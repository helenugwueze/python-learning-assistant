from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from pathlib import Path
import json, contextlib, io, importlib.util, os
from dotenv import load_dotenv
import psycopg

import secrets
from psycopg.rows import dict_row
from authlib.integrations.flask_client import OAuth

BASE = Path(__file__).resolve().parent
load_dotenv(BASE / ".env")
DATA = BASE / 'data'
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "local-development-key")
oauth = OAuth(app)

print("Google Client ID loaded:", bool(os.environ.get("GOOGLE_CLIENT_ID")))
print("Google Client Secret loaded:", bool(os.environ.get("GOOGLE_CLIENT_SECRET")))

google = oauth.register(
    name='google',
    client_id=os.environ.get('GOOGLE_CLIENT_ID'),
    client_secret=os.environ.get('GOOGLE_CLIENT_SECRET'),
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile'
    }
)

LESSON_TITLES = {
 1:'Introduction to Python',2:'Variables',3:'Data Types',4:'Strings',5:'Numbers',
 6:'Type Conversion',7:'Operators',8:'User Input',9:'Output',10:'Comments',
 11:'Conditional Statements',12:'Comparison Operators',13:'Logical Operators',
 14:'For Loops',15:'While Loops',16:'Break and Continue',17:'Nested Loops',
 18:'Lists',19:'Tuples',20:'Sets',21:'Dictionaries',22:'Functions',23:'List Comprehensions'
}

def connect():
    return psycopg.connect(
        os.environ["DATABASE_URL"],
        row_factory=dict_row
    )

def init_db():
    with connect() as con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS google_accounts (
                id BIGSERIAL PRIMARY KEY,
                user_id BIGINT NOT NULL REFERENCES users(id),
                google_sub TEXT UNIQUE NOT NULL,
                email TEXT NOT NULL
            )
        """)

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
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')

        if not username or not email or len(password) < 8:
            flash('Enter a username, email, and a password with at least 8 characters.', 'error')
        else:
            try:
                with connect() as con:
                    con.execute(
                        'INSERT INTO users(username, email, password) VALUES(%s, %s, %s)',
                        (username, email, generate_password_hash(password))
                    )

                flash('Account created. Please sign in.', 'success')
                return redirect(url_for('login'))

            except psycopg.errors.UniqueViolation:
                flash('That username or email is already in use.', 'error')

    return render_template('auth.html', mode='register')



@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form.get('username','').strip(); password=request.form.get('password','')
        with connect() as con:
            user = con.execute(
                'SELECT * FROM users WHERE username = %s',
                (username,)
            ).fetchone()
        if user and check_password_hash(user['password'],password):
            session.clear(); session['user_id']=user['id']; session['username']=user['username']; return redirect(url_for('dashboard'))
        flash('Incorrect username or password.','error')
    return render_template('auth.html', mode='login')



@app.route('/google/login')
def google_login():
    redirect_uri = url_for('google_callback', _external=True)

    return google.authorize_redirect(
        redirect_uri,
        prompt='select_account'
    )

@app.route('/google/callback')
def google_callback():
    token = google.authorize_access_token()
    user_info = token['userinfo']

    if not user_info.get('email_verified'):
        flash('Google email could not be verified.', 'error')
        return redirect(url_for('login'))

    google_sub = user_info['sub']
    email = user_info['email'].strip().lower()

    with connect() as con:
        account = con.execute(
            'SELECT user_id FROM google_accounts WHERE google_sub = %s',
            (google_sub,)
        ).fetchone()

        if account:
            user = con.execute(
                'SELECT id, username FROM users WHERE id = %s',
                (account['user_id'],)
            ).fetchone()

            if user:
                session.clear()
                session['user_id'] = user['id']
                session['username'] = user['username']
                return redirect(url_for('dashboard'))
   
        else:
            existing_user = con.execute(
                'SELECT id FROM users WHERE email = %s',
                (email,)
            ).fetchone()

            base_username = email.split('@')[0]
            username = f"{base_username}_{secrets.token_hex(3)}"


            if existing_user:
                flash('An account with this email already exists. Please log in normally.', 'error')
                return redirect(url_for('login'))
            user = con.execute(
                'INSERT INTO users(username, email, password) VALUES(%s, %s, %s) RETURNING id, username',
                (username, email, generate_password_hash(secrets.token_urlsafe(32)))
            ).fetchone()    
            con.execute(
                'INSERT INTO google_accounts(user_id, google_sub, email) VALUES(%s, %s, %s)',
                (user['id'], google_sub, email)
            )            

        session.clear()
        session['user_id'] = user['id']
        session['username'] = user['username']
    return redirect(url_for('dashboard'))



@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.after_request
def prevent_cache(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    return response

@app.route('/dashboard')
@login_required
def dashboard():
    uid = current_user()

    with connect() as con:
        done = con.execute(
            'SELECT COUNT(*) AS n FROM completed WHERE user_id = %s',
            (uid,)
        ).fetchone()['n']

        result = con.execute(
            'SELECT score, total, created_at FROM quiz_results WHERE user_id = %s ORDER BY id DESC LIMIT 1',
            (uid,)
        ).fetchone()

    return render_template(
        'dashboard.html',
        total=23,
        done=done,
        percent=round(done/23*100),
        last_result=result
    )

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

@app.route('/lessons')
@login_required
def lessons():
    uid = current_user()

    with connect() as con:
        rows = con.execute(
            'SELECT lesson FROM completed WHERE user_id = %s',
            (uid,)
        ).fetchall()

    done = {row['lesson'] for row in rows}

    return render_template('lessons.html', lessons=LESSON_TITLES, done=done)

@app.route('/lessons/<int:number>')
@login_required
def lesson(number):
    if number not in LESSON_TITLES:
        return redirect(url_for('lessons'))

    with connect() as con:
        done = con.execute(
            'SELECT 1 FROM completed WHERE user_id = %s AND lesson = %s',
            (current_user(), number)
        ).fetchone()

    return render_template(
        'lesson.html',
        number=number,
        title=LESSON_TITLES[number],
        content=lesson_text(number),
        done=bool(done)
    )
    
@app.route('/lessons/<int:number>/complete', methods=['POST'])
@login_required
def complete_lesson(number):
    if number not in LESSON_TITLES:
        return redirect(url_for('lessons'))

    with connect() as con:
        con.execute(
            'INSERT INTO completed (user_id, lesson) VALUES (%s, %s) ON CONFLICT DO NOTHING',
            (current_user(), number)
        )

    return redirect(url_for('lesson', number=number))


@app.route('/quiz', methods=['GET','POST'])
@login_required
def quiz():
    questions=json.loads((DATA/'questions.json').read_text())
    if request.method=='POST':
        score=sum(1 for i,q in enumerate(questions) if request.form.get(f'q{i}')==q['answer'])
        with connect() as con:
            con.execute(
                'INSERT INTO quiz_results(user_id, score, total) VALUES(%s, %s, %s)',
                (current_user(), score, len(questions))
            )

        return render_template('quiz_result.html',score=score,total=len(questions))
    return render_template('quiz.html',questions=questions)

@app.route('/progress')
@login_required
def progress():
    uid = current_user()

    with connect() as con:
        done = con.execute(
            'SELECT lesson FROM completed WHERE user_id = %s ORDER BY lesson',
            (uid,)
        ).fetchall()

        results = con.execute(
            'SELECT score, total, created_at FROM quiz_results WHERE user_id = %s ORDER BY id DESC LIMIT 5',
            (uid,)
        ).fetchall()

    return render_template(
        'progress.html',
        done=[r['lesson'] for r in done],
        total=23,
        results=results
    )


init_db()

if __name__ == '__main__':
    app.run(debug=True, port=5001)
