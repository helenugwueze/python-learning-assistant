from lessons.lesson_23 import display_lesson_23
from lessons.lesson_22 import display_lesson_22
from lessons.lesson_21 import display_lesson_21
from lessons.lesson_20 import display_lesson_20
from lessons.lesson_19 import display_lesson_19
from lessons.lesson_18 import display_lesson_18
from lessons.lesson_17 import display_lesson_17
from lessons.lesson_16 import display_lesson_16
from lessons.lesson_15 import display_lesson_15
from lessons.lesson_14 import display_lesson_14
from lessons.lesson_13 import display_lesson_13
from lessons.lesson_12 import display_lesson_12
from lessons.lesson_11 import display_lesson_11
def welcome():
    print("====== PYTHON LEARNING ASSISTANT ======")
    print("Welcome! Learn Python step by step.")

    name = input("What is your name? ")
    while name == "":
        print("Name cannot be empty.")
        name = input("Please enter your name: ")
    print("welcome", name)    

welcome()

def learn_python():
    print("\n========== PYTHON TOPICS ==========")
    topics = {
        "1": "Introduction to Python",
        "2": "Variables",
        "3": "Data Types",
        "4": "Strings",
        "5": "Numbers",
        "6": "Type Conversion",
        "7": "Operators",
        "8": "User Input",
        "9": "Output",
        "10": "Comments",
        "11": "Conditional statements",
        "12": "Comparsion operators in python",
        "13": "Logical operators in python",
        "14": "For loops in python",
        "15": "While loops in python",
        "16": "Break and continue statement",
        "17": "Nested loops python",
        "18": "Lists in python",
        "19": "Tuples in python",
        "20": "Set in python",
        "21": "Dictionaries in python",
        "22": "Function in python",
        "23": "List comprehension in python"

    }
    for key, value in topics.items():
        print(f"{key}. {value}")

    print("Welcome to Python lessons!")
    topic_choice = input("Enter a topic number to learn: ")

    if topic_choice == "1":
        print("\nWhat is Python?")
        print("""
         INTRODUCTION TO PYTHON

 1. INTRODUCTION

Python is one of the most popular programming languages in the world. It is widely used by beginners, software developers, data scientists, and artificial intelligence engineers.

Python was created by Guido van Rossum and was first released in 1991.

Python was designed to make programming easier to read, understand, and write.

Today, Python is used to develop websites, desktop applications, games, automation tools, and artificial intelligence systems.

2. DEFINITION

Python is a high-level, general-purpose programming language known for its simple and readable syntax.

A programming language is a language that allows humans to communicate instructions to a computer.

 3. EXPLANATION

Let's understand some important features of Python.

 A. Python is a High-Level Language

A high-level programming language is designed to be easier for humans to read and understand.

For example:

print("Hello World")

This instruction tells Python to display Hello World on the screen.

 B. Python is Easy to Read

Python uses simple words and a clean structure.

This makes it easier for beginners to understand what their programs are doing.

 C. Python is Interpreted

Python is commonly described as an interpreted language.

Its interpreter executes Python programs and reports errors when something goes wrong.

 D. Python is General-Purpose

Python can be used for different types of projects.

Examples include:
- Web development.
- Artificial intelligence.
- Machine learning.
- Data analysis.
- Automation.
- Software development.

 E. Python is Cross-Platform

Python can run on different operating systems, including:
- Windows.
- Linux.
- macOS.

4. EXAMPLES

 Example 1: Displaying a Message

Code:

print("Hello World")

Explanation:

- print() is a built-in Python function.
- "Hello World" is the text we want to display.
- The quotation marks tell Python that the content is a string.

Output:

Hello World

Example 2: Displaying Multiple Messages

Code:

print("Welcome to Python")
print("Python is easy to learn")
print("I am learning programming")

Output:

Welcome to Python
Python is easy to learn
I am learning programming

Explanation:

Each print() statement displays a message on the screen.

Python executes the instructions from top to bottom.

 5. SUMMARY

Python is a popular, high-level, general-purpose programming language.

Important things to remember:

1. Python was created by Guido van Rossum.
2. Python was first released in 1991.
3. Python has simple and readable syntax.
4. Python is commonly used as an interpreted language.
5. Python works on different operating systems.
6. Python is used in web development, automation, data science, and artificial intelligence.
7. The print() function displays information on the screen.

**Remember:** Python is a programming language that allows us to give instructions to computers..""")
    elif topic_choice == "2":
        print("""
         LESSON 2: VARIABLES IN PYTHON

1. INTRODUCTION

Variables are one of the most important concepts in Python programming.

When writing programs, we often need to store information so that we can use it later.

For example, a program may need to remember a person's name, age, email address, or school grade.

Python uses variables to store and manage this information.

Variables make programs more flexible because the information stored in them can be accessed and changed when needed.

2. DEFINITION

A variable is a named storage location used to hold a value in a computer program.

In Python, a variable is created when you assign a value to a name.

Example:

name = "Helen"

Here:
- name is the variable.
- "Helen" is the value stored in the variable.
- The equal sign (=) is the assignment operator.

3. EXPLANATION

Let's understand variables in more detail.

A. How Variables Work

A variable gives a name to a value so that we can use that value whenever we need it.

Example:

name = "Helen"

print(name)

Output:

Helen

Explanation:

First, Python assigns the value "Helen" to the variable called name.

Next, print(name) displays the value stored in that variable.

 B. Creating Variables

In Python, you do not need to declare a variable before using it.

You simply choose a name and assign a value to it.

Examples:

name = "John"
age = 25
country = "Nigeria"
height = 1.75

Each variable stores a different value.

 C. Rules for Naming Variables

Python has rules for naming variables.

1. A variable name must start with a letter or an underscore.
2. A variable name cannot start with a number.
3. Variable names can contain letters, numbers, and underscores.
4. Variable names cannot contain spaces.
5. Variable names are case-sensitive.
6. Python keywords cannot be used as variable names.

Valid variable names:

name = "Helen"
age = 20
student_name = "John"
_age = 25
score1 = 90

Invalid variable names:

1name = "Helen"
student name = "John"
my-age = 20

These names are invalid because they break Python's naming rules.

 D. Variables Are Changeable

The value stored in a variable can be changed during program execution.

Example:

age = 20

age = 25

print(age)

Output:

25

Explanation:

Initially, age stores 20.

Later, the value is changed to 25.

When Python prints age, it displays the latest value.

 E. Assigning Multiple Variables

Python allows you to assign values to multiple variables in one statement.

Example:

name, age, country = "Helen", 20, "Nigeria"

print(name)
print(age)
print(country)

Output:

Helen
20
Nigeria

Each variable receives its corresponding value.

 F. Assigning the Same Value to Multiple Variables

You can also assign the same value to different variables.

Example:

x = y = z = 10

print(x)
print(y)
print(z)

Output:

10
10
10

All three variables contain the value 10.

 G. Variables Can Store Different Data Types

Variables can store different types of values.

Examples:

name = "Helen"
age = 20
height = 1.65
is_student = True

Explanation:

- name stores a string.
- age stores an integer.
- height stores a float.
- is_student stores a Boolean value.

 4. PRACTICAL EXAMPLES

 Example 1: Storing a Name

Code:

name = "Helen"

print("My name is", name)

Output:

My name is Helen

Explanation:

The variable name stores the text "Helen".

The print() function displays the message together with the stored value.

 Example 2: Storing a Student's Information

Code:

name = "Helen"
age = 20
course = "Python Programming"

print("Student Name:", name)
print("Age:", age)
print("Course:", course)

Output:

Student Name: Helen
Age: 20
Course: Python Programming

Explanation:

The program creates three variables and stores different information in them.

Each variable can be accessed independently.

 Example 3: Updating a Variable

Code:

score = 50

print("Old score:", score)

score = 85

print("New score:", score)

Output:

Old score: 50
New score: 85

Explanation:

The score variable initially stores 50.

Later, its value changes to 85.

Python displays the updated value when the variable is printed again.

 Example 4: Using Variables in Calculations

Code:

first_number = 10
second_number = 5

total = first_number + second_number

print("Total:", total)

Output:

Total: 15

Explanation:

The program stores two numbers in separate variables.

It adds the values together and stores the result in another variable called total.

The print() function displays the result.

 5. SUMMARY

Variables are named storage locations used to hold values in Python programs.

Important things to remember:

1. Variables store information.
2. A variable is created when a value is assigned to it.
3. The equal sign (=) is the assignment operator.
4. Variable names must follow Python's naming rules.
5. Variable names are case-sensitive.
6. Variables can store different data types.
7. Variable values can be changed during program execution.
8. Python allows multiple variables to be assigned in one statement.
9. Variables can be used in calculations.
10. The print() function can display the value stored in a variable.

**REMEMBER:** A variable is a name that refers to a value stored in a Python program.
    """)

    elif topic_choice == "3":
        print("""
        LESSON 3: DATA TYPES IN PYTHON

1. INTRODUCTION

In Python, data types help us understand the different kinds of information we work with. Every value in Python has a data type. Data types tell Python whether a value is text, a number, a collection of items, or a true/false value.

2. STRING (str)

Introduction:
Strings are used whenever we want to work with text in Python.

Definition:
A string is a data type used to store letters, words, sentences, and other characters.

Explanation:
Strings are written inside quotation marks. Python accepts both single and double quotation marks.

Example:
name = "Helen"
country = 'Nigeria'

print(name)
print(country)

Summary:
A string stores text inside quotation marks.

3. INTEGER (int)

Introduction:
Python allows us to work with whole numbers using integers.

Definition:
An integer is a data type used to store whole numbers without decimal points.

Explanation:
Integers can be positive, negative, or zero.

Example:
age = 25
temperature = -5
score = 100

print(age)

Summary:
An integer stores whole numbers without decimal points.

4. FLOAT (float)

Introduction:
Sometimes we need to work with numbers that contain decimal points. Python uses floats for this purpose.

Definition:
A float is a data type used to store numbers with decimal points.

Explanation:
Floats are useful when working with measurements, prices, and calculations that require decimal values.

Example:
height = 1.65
price = 250.50
weight = 60.5

print(height)

Summary:
A float stores numbers with decimal points.

5. BOOLEAN (bool)

Introduction:
Sometimes a program needs to make decisions based on whether something is true or false.

Definition:
A Boolean is a data type that stores only two values: True or False.

Explanation:
Booleans are commonly used in conditions and decision-making in Python.

Example:
is_student = True
is_married = False

print(is_student)

Summary:
A Boolean stores either True or False.

6. LIST (list)

Introduction:
Sometimes we need to store several values in one variable. Python provides lists to help us do this.

Definition:
A list is a data type used to store multiple items in a single variable.

Explanation:
Lists are written inside square brackets []. They are ordered and can be changed after creation.

Example:
fruits = ["apple", "banana", "orange"]

print(fruits)

Summary:
A list stores multiple items in an ordered and changeable collection.

7. TUPLE (tuple)

Introduction:
Python also provides a way to store multiple items that should not be changed.

Definition:
A tuple is a data type used to store multiple items in one variable.

Explanation:
Tuples are written inside parentheses (). They are ordered but cannot be changed after creation.

Example:
colors = ("red", "blue", "green")

print(colors)

Summary:
A tuple stores multiple items in an ordered collection that cannot be changed.

8. DICTIONARY (dict)

Introduction:
Sometimes we need to store information using labels and their corresponding values. Python dictionaries help us do this.

Definition:
A dictionary is a data type that stores information in key-value pairs.

Explanation:
Dictionaries are written inside curly brackets {}. Each key is connected to a value using a colon.

Example:
student = {
    "name": "Helen",
    "age": 25,
    "country": "Nigeria"
}

print(student)

Summary:
A dictionary stores information in key-value pairs.

9. SET (set)

Introduction:
Sometimes we want to store multiple items without keeping duplicate values. Python provides sets for this purpose.

Definition:
A set is a data type used to store unique items in a collection.

Explanation:
Sets are written inside curly brackets {}. They do not allow duplicate values and do not maintain a fixed order.

Example:
numbers = {1, 2, 3, 4, 4}

print(numbers)

Summary:
A set stores unique items without duplicates.

10. GENERAL SUMMARY

Python has different data types for storing different kinds of information.

- str stores text.
- int stores whole numbers.
- float stores decimal numbers.
- bool stores True or False.
- list stores ordered and changeable collections.
- tuple stores ordered and unchangeable collections.
- dict stores key-value pairs.
- set stores unique items.

Understanding data types helps us choose the correct way to store and work with information in Python.
    """)
    elif topic_choice == "4":
        print("""
        LESSON 4: STRINGS IN PYTHON

1. INTRODUCTION

Strings are used to work with text in Python.

2. DEFINITION

A string is a collection of characters enclosed in quotation marks.

3. EXPLANATION

Strings can contain letters, numbers, symbols, and spaces.

Python uses single or double quotation marks.

4. EXAMPLES

name = "Helen"
country = "Nigeria"

print(name)
print(country)

5. SUMMARY

Strings store text using quotation marks.
    """)
    elif topic_choice == "5":
        print("""
        LESSON 5: NUMBERS IN PYTHON

1. INTRODUCTION

Python allows us to work with numbers to perform calculations.

2. DEFINITION

Numbers are values used for counting, measuring, and calculations.

3. TYPES OF NUMBERS

A. INTEGER (int)

Definition:
Integers are whole numbers without decimal points.

Example:
age = 20

B. FLOAT (float)

Definition:
Floats are numbers with decimal points.

Example:
price = 50.5

4. EXPLANATION

Python supports basic mathematical operations:

- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)

5. EXAMPLES

first_number = 10
second_number = 5

print(first_number + second_number)
print(first_number - second_number)
print(first_number * second_number)
print(first_number / second_number)

6. SUMMARY

Python uses integers and floats to work with numbers and perform calculations.
    """)
    elif topic_choice == "6":
        print("""
        LESSON 6: TYPE CONVERSION IN PYTHON

1. INTRODUCTION

Sometimes we need to change one data type into another.

2. DEFINITION

Type conversion is changing a value from one data type to another.

3. EXPLANATION

Python provides functions for converting data types:

- int() converts to an integer.
- float() converts to a float.
- str() converts to a string.

4. EXAMPLES

age = "20"

new_age = int(age)

print(new_age)

price = 50

new_price = float(price)

print(new_price)

5. SUMMARY

Type conversion helps us change values from one data type to another.
  """)
    elif topic_choice == "7":
        print("""
        LESSON 7: OPERATORS IN PYTHON

1. INTRODUCTION

Operators help us perform calculations and compare values in Python.

2. DEFINITION

An operator is a symbol used to perform an operation on values.

3. TYPES OF OPERATORS

A. Arithmetic Operators

Used for mathematical calculations.

- + Addition
- - Subtraction
- * Multiplication
- / Division
- % Modulus (remainder)

B. Comparison Operators

Used to compare values.

- == Equal to
- != Not equal to
- > Greater than
- < Less than

C. Logical Operators

Used to combine conditions.

- and
- or
- not

4. EXAMPLES

a = 10
b = 5

print(a + b)
print(a > b)
print(a == b)

5. SUMMARY

Operators help Python perform calculations, comparisons, and logical operations.
    """)
    elif  topic_choice == "8":
        print("""
        LESSON 8: USER INPUT IN PYTHON

1. INTRODUCTION

Python allows users to enter information into a program.

2. DEFINITION

User input is information provided by a user while a program is running.

3. EXPLANATION

Python uses the input() function to receive information from users.

4. EXAMPLES

name = input("What is your name? ")

print("Welcome", name)

5. SUMMARY

The input() function allows Python programs to receive information from users.
    """)
    elif topic_choice == "9":
        print("""
        LESSON 9: OUTPUT IN PYTHON

1. INTRODUCTION

Python can display information on the screen.

2. DEFINITION

Output is the information a program displays to the user.

3. EXPLANATION

Python uses the print() function to display text, numbers, and variable values.

4. EXAMPLES

name = "Helen"

print("Hello")
print(name)
print(20 + 5)

5. SUMMARY

The print() function displays information on the screen.
    """)
    elif topic_choice == "10":
        print("""
        LESSON 10: COMMENTS IN PYTHON

1. INTRODUCTION

Comments help programmers explain their code.

2. DEFINITION

A comment is a note in code that Python does not execute.

3. EXPLANATION

Python uses the hash symbol (#) to write comments.

Comments make code easier to understand.

4. EXAMPLES

# This is a comment

name = "Helen"

# Display the name
print(name)

5. SUMMARY

Comments explain code and help programmers understand their programs.
        """)
    elif topic_choice == "11":
        display_lesson_11()

    elif topic_choice == "12":
        display_lesson_12()

    elif topic_choice == "13":
        display_lesson_13()

    elif topic_choice == "14":
        display_lesson_14() 

    elif topic_choice == "15":
        display_lesson_15()

    elif topic_choice == "16":
        display_lesson_16()

    elif topic_choice == "17":
        display_lesson_17()

    elif topic_choice == "18":
        display_lesson_18()

    elif topic_choice == "19":
        display_lesson_19()

    elif topic_choice == "20":
        display_lesson_20()

    elif topic_choice == "21":
        display_lesson_21()

    elif topic_choice == "22":
        display_lesson_22()
    elif topic_choice == "23":
        display_lesson_23()              



    elif topic_choice in topics:
        print("topic:", topics[topic_choice])
            
    else:
        print("Invalid topic number.")

 

def display_menu():
    
    choice = None
    while choice != "4":

        print("\n========== MAIN MENU ==========")
        menu = {
        "1": "learn python",
        "2": "take a quiz",
        "3": "view progress",
        "4": "exit"
        }
        for key, value in menu.items():
            print(f"{key}. {value.title()}")

        choice = input("enter your choice (1-4):")
        print("You selected:", choice)

        if choice == "1":
            learn_python()
           
        elif choice == "2":
            take_quiz()
           
           
        elif choice == "3":
            view_progress()
           
        elif choice == "4":
            print("Goodbye")
           
        else:
            print("Invalid choice. Please select 1-4.") 


def take_quiz():
    print("\n========== PYTHON QUIZ ==========")
    print("Welcome to the Python quiz!")
    print("Answer all 150 questions.")
    print("Choose your answer from A, B, C, or D.")

    questions = [

        # LESSON 1: INTRODUCTION TO PYTHON

        {
            "question": "Who created Python?",
            "options": ["A. James Gosling", "B. Guido van Rossum", "C. Dennis Ritchie", "D. Brendan Eich"],
            "answer": "B"
        },
        {
            "question": "In which year was Python first released?",
            "options": ["A. 1985", "B. 1995", "C. 1991", "D. 2000"],
            "answer": "C"
        },
        {
            "question": "What type of programming language is Python?",
            "options": ["A. High-level", "B. Machine-level", "C. Assembly-level", "D. Binary-level"],
            "answer": "A"
        },
        {
            "question": "Which of these is a major feature of Python?",
            "options": ["A. Difficult syntax", "B. Readable syntax", "C. Machine-only language", "D. No variables"],
            "answer": "B"
        },
        {
            "question": "Python is commonly used for which of these?",
            "options": ["A. Web development", "B. Data analysis", "C. Artificial intelligence", "D. All of the above"],
            "answer": "D"
        },
        {
            "question": "What does cross-platform mean?",
            "options": ["A. Runs on one computer only", "B. Works on different operating systems", "C. Works without code", "D. Runs only online"],
            "answer": "B"
        },

        # LESSON 2: VARIABLES

        {
            "question": "What is a variable in Python?",
            "options": ["A. A storage location for data", "B. A type of loop", "C. A Python error", "D. A comment"],
            "answer": "A"
        },
        {
            "question": "Which symbol is used to assign a value to a variable?",
            "options": ["A. ==", "B. =", "C. !=", "D. >"],
            "answer": "B"
        },
        {
            "question": "Which is a valid Python variable name?",
            "options": ["A. 2name", "B. first-name", "C. first_name", "D. first name"],
            "answer": "C"
        },
        {
            "question": "What is the output of name = 'Helen'; print(name)?",
            "options": ["A. name", "B. Helen", "C. 'name'", "D. Error"],
            "answer": "B"
        },
        {
            "question": "Can a Python variable's value be changed?",
            "options": ["A. No", "B. Only once", "C. Yes", "D. Only with a loop"],
            "answer": "C"
        },
        {
            "question": "Which naming style uses lowercase words separated by underscores?",
            "options": ["A. camelCase", "B. snake_case", "C. PascalCase", "D. UPPERCASE"],
            "answer": "B"
        },

        # LESSON 3: DATA TYPES

        {
            "question": "Which data type stores text?",
            "options": ["A. int", "B. float", "C. str", "D. bool"],
            "answer": "C"
        },
        {
            "question": "Which data type stores whole numbers?",
            "options": ["A. int", "B. str", "C. float", "D. list"],
            "answer": "A"
        },
        {
            "question": "Which data type stores decimal numbers?",
            "options": ["A. int", "B. float", "C. bool", "D. str"],
            "answer": "B"
        },
        {
            "question": "What are the two Boolean values in Python?",
            "options": ["A. Yes and No", "B. 1 and 2", "C. True and False", "D. On and Off"],
            "answer": "C"
        },
        {
            "question": "What is the data type of 25?",
            "options": ["A. str", "B. int", "C. float", "D. bool"],
            "answer": "B"
        },
        {
            "question": "What is the data type of '25'?",
            "options": ["A. int", "B. float", "C. str", "D. bool"],
            "answer": "C"
        },

        # LESSON 4: STRINGS

        {
            "question": "What is a string in Python?",
            "options": ["A. A collection of numbers only", "B. A sequence of characters", "C. A loop", "D. A condition"],
            "answer": "B"
        },
        {
            "question": "Which symbol can be used to create a string?",
            "options": ["A. Quotes", "B. Curly brackets only", "C. Square brackets only", "D. Greater-than symbol"],
            "answer": "A"
        },
        {
            "question": "What does len('Python') return?",
            "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
            "answer": "B"
        },
        {
            "question": "Which method converts a string to uppercase?",
            "options": ["A. lower()", "B. title()", "C. upper()", "D. strip()"],
            "answer": "C"
        },
        {
            "question": "Which method removes whitespace from the beginning and end of a string?",
            "options": ["A. remove()", "B. strip()", "C. delete()", "D. split()"],
            "answer": "B"
        },
        {
            "question": "What does 'hello'.upper() return?",
            "options": ["A. hello", "B. Hello", "C. HELLO", "D. hELLO"],
            "answer": "C"
        },

        # LESSON 5: NUMBERS

        {
            "question": "Which operator performs addition?",
            "options": ["A. +", "B. -", "C. *", "D. /"],
            "answer": "A"
        },
        {
            "question": "What is 10 + 5?",
            "options": ["A. 10", "B. 15", "C. 20", "D. 5"],
            "answer": "B"
        },
        {
            "question": "Which operator performs multiplication?",
            "options": ["A. /", "B. +", "C. *", "D. %"],
            "answer": "C"
        },
        {
            "question": "What is the result of 20 / 4?",
            "options": ["A. 4", "B. 5.0", "C. 6", "D. 8"],
            "answer": "B"
        },
        {
            "question": "Which operator returns the remainder of a division?",
            "options": ["A. //", "B. **", "C. %", "D. /"],
            "answer": "C"
        },
        {
            "question": "What is the result of 2 ** 3?",
            "options": ["A. 5", "B. 6", "C. 8", "D. 9"],
            "answer": "C"
        },

        # LESSON 6: TYPE CONVERSION

        {
            "question": "What is type conversion?",
            "options": ["A. Changing a value from one data type to another", "B. Creating a loop", "C. Deleting a variable", "D. Printing a value"],
            "answer": "A"
        },
        {
            "question": "Which function converts a value to an integer?",
            "options": ["A. str()", "B. int()", "C. float()", "D. bool()"],
            "answer": "B"
        },
        {
            "question": "What does str(100) return?",
            "options": ["A. 100 as an integer", "B. 100.0", "C. '100' as a string", "D. True"],
            "answer": "C"
        },
        {
            "question": "Which function converts a number to a floating-point value?",
            "options": ["A. int()", "B. float()", "C. str()", "D. list()"],
            "answer": "B"
        },
        {
            "question": "What is the result of int('25')?",
            "options": ["A. '25'", "B. 25", "C. 25.0", "D. Error"],
            "answer": "B"
        },
        {
            "question": "What happens when int('hello') is executed?",
            "options": ["A. It returns 0", "B. It returns True", "C. It raises a ValueError", "D. It returns 'hello'"],
            "answer": "C"
        },

        # LESSON 7: OPERATORS

        {
            "question": "Which operator is used for subtraction?",
            "options": ["A. +", "B. -", "C. *", "D. /"],
            "answer": "B"
        },
        {
            "question": "Which operator checks whether two values are not equal?",
            "options": ["A. ==", "B. =", "C. !=", "D. >="],
            "answer": "C"
        },
        {
            "question": "What is the result of 10 > 5?",
            "options": ["A. True", "B. False", "C. 10", "D. 5"],
            "answer": "A"
        },
        {
            "question": "Which operator performs floor division?",
            "options": ["A. /", "B. %", "C. //", "D. **"],
            "answer": "C"
        },
        {
            "question": "What does the += operator do?",
            "options": ["A. Compares two values", "B. Adds a value and assigns the result", "C. Divides two values", "D. Removes a value"],
            "answer": "B"
        },
        {
            "question": "Which operator checks whether a value is greater than or equal to another?",
            "options": ["A. <=", "B. ==", "C. >=", "D. !="],
            "answer": "C"
        },

        # LESSON 8: USER INPUT

        {
            "question": "Which function collects information from a user?",
            "options": ["A. print()", "B. input()", "C. type()", "D. len()"],
            "answer": "B"
        },
        {
            "question": "What data type does input() return by default?",
            "options": ["A. int", "B. float", "C. str", "D. bool"],
            "answer": "C"
        },
        {
            "question": "Which code asks the user for their name?",
            "options": ["A. print('Name')", "B. input('Enter your name: ')", "C. len('Name')", "D. type('Name')"],
            "answer": "B"
        },
        {
            "question": "How can you convert a user's input into an integer?",
            "options": ["A. input(int)", "B. int(input())", "C. str(input())", "D. print(input())"],
            "answer": "B"
        },
        {
            "question": "Which variable can store a user's name?",
            "options": ["A. name = input()", "B. name == input()", "C. input == name", "D. name + input"],
            "answer": "A"
        },
        {
            "question": "Why should user input sometimes be validated?",
            "options": ["A. To make the program longer", "B. To check that the input is acceptable", "C. To delete the input", "D. To stop Python"],
            "answer": "B"
        },

        # LESSON 9: OUTPUT

        {
            "question": "Which function displays information on the screen?",
            "options": ["A. input()", "B. print()", "C. type()", "D. int()"],
            "answer": "B"
        },
        {
            "question": "What is the output of print('Hello')?",
            "options": ["A. 'print'", "B. Hello", "C. Error", "D. Nothing"],
            "answer": "B"
        },
        {
            "question": "Which argument changes the separator between printed values?",
            "options": ["A. end", "B. sep", "C. start", "D. split"],
            "answer": "B"
        },
        {
            "question": "Which print() argument controls what is printed at the end?",
            "options": ["A. sep", "B. stop", "C. end", "D. finish"],
            "answer": "C"
        },
        {
            "question": "What does print('Hello', 'World') display by default?",
            "options": ["A. HelloWorld", "B. Hello World", "C. Hello,World", "D. Error"],
            "answer": "B"
        },
        {
            "question": "Which is an example of formatted output using an f-string?",
            "options": ["A. print(f'Hello {name}')", "B. print('Hello name')", "C. input(f'name')", "D. str.print(name)"],
            "answer": "A"
        },

        # LESSON 10: COMMENTS

        {
            "question": "What is the purpose of comments in Python?",
            "options": ["A. To explain code", "B. To execute loops", "C. To create variables", "D. To collect input"],
            "answer": "A"
        },
        {
            "question": "Which symbol starts a single-line comment?",
            "options": ["A. //", "B. #", "C. /*", "D. --"],
            "answer": "B"
        },
        {
            "question": "Does Python execute a normal comment?",
            "options": ["A. Yes", "B. No", "C. Only in loops", "D. Only in functions"],
            "answer": "B"
        },
        {
            "question": "Which is a valid Python comment?",
            "options": ["A. // This is a comment", "B. # This is a comment", "C. <!-- Comment -->", "D. ** Comment"],
            "answer": "B"
        },
        {
            "question": "Why should comments be meaningful?",
            "options": ["A. To make code harder to read", "B. To help explain important code", "C. To replace every variable", "D. To stop errors automatically"],
            "answer": "B"
        },
        {
            "question": "What is a docstring commonly used for?",
            "options": ["A. Documenting a function, class, or module", "B. Creating a number", "C. Starting a loop", "D. Collecting user input"],
            "answer": "A"
        },

        # LESSON 11: CONDITIONAL STATEMENTS

        {
            "question": "What is the purpose of an if statement?",
            "options": ["A. To repeat code", "B. To make decisions", "C. To create a list", "D. To define a function"],
            "answer": "B"
        },
        {
            "question": "Which keyword runs code when an if condition is false?",
            "options": ["A. for", "B. while", "C. else", "D. break"],
            "answer": "C"
        },
        {
            "question": "Which keyword checks another condition after an if?",
            "options": ["A. elif", "B. return", "C. continue", "D. def"],
            "answer": "A"
        },
        {
            "question": "What must follow an if condition before its code block?",
            "options": ["A. Semicolon", "B. Colon", "C. Comma", "D. Full stop"],
            "answer": "B"
        },
        {
            "question": "What happens when an if condition evaluates to True?",
            "options": ["A. Its code block executes", "B. Python exits", "C. The program deletes the condition", "D. The code is ignored"],
            "answer": "A"
        },
        {
            "question": "What is a nested if statement?",
            "options": ["A. An if statement inside another if statement", "B. An if statement without a condition", "C. A loop inside a list", "D. A function without a name"],
            "answer": "A"
        },
        {
            "question": "Which value represents a condition that is not satisfied?",
            "options": ["A. True", "B. False", "C. None of the above", "D. Both True and False"],
            "answer": "B"
        },

        # LESSON 12: COMPARISON OPERATORS

        {
            "question": "What does the == operator check?",
            "options": ["A. Assignment", "B. Equality", "C. Addition", "D. Division"],
            "answer": "B"
        },
        {
            "question": "What is the result of 8 < 3?",
            "options": ["A. True", "B. False", "C. 8", "D. 3"],
            "answer": "B"
        },
        {
            "question": "Which operator means less than or equal to?",
            "options": ["A. >=", "B. <=", "C. !=", "D. =="],
            "answer": "B"
        },
        {
            "question": "What is the result of 10 != 5?",
            "options": ["A. True", "B. False", "C. 5", "D. 10"],
            "answer": "A"
        },
        {
            "question": "What type of value do comparison operators return?",
            "options": ["A. String", "B. List", "C. Boolean", "D. Dictionary"],
            "answer": "C"
        },
        {
            "question": "Which operator checks whether the left value is greater than the right value?",
            "options": ["A. <", "B. >", "C. ==", "D. !="],
            "answer": "B"
        },
        {
            "question": "What is the result of 7 >= 7?",
            "options": ["A. True", "B. False", "C. 7", "D. Error"],
            "answer": "A"
        },

        # LESSON 13: LOGICAL OPERATORS

        {
            "question": "Which logical operator requires both conditions to be True?",
            "options": ["A. or", "B. not", "C. and", "D. in"],
            "answer": "C"
        },
        {
            "question": "Which logical operator returns True when at least one condition is True?",
            "options": ["A. and", "B. or", "C. not", "D. is"],
            "answer": "B"
        },
        {
            "question": "What does the not operator do?",
            "options": ["A. Adds two values", "B. Reverses a Boolean value", "C. Compares strings", "D. Creates a loop"],
            "answer": "B"
        },
        {
            "question": "What is True and False?",
            "options": ["A. True", "B. False", "C. None", "D. Error"],
            "answer": "B"
        },
        {
            "question": "What is True or False?",
            "options": ["A. True", "B. False", "C. None", "D. Error"],
            "answer": "A"
        },
        {
            "question": "What is not True?",
            "options": ["A. True", "B. False", "C. None", "D. 1"],
            "answer": "B"
        },
        {
            "question": "Which operator is suitable when either of two conditions may be satisfied?",
            "options": ["A. and", "B. or", "C. not", "D. =="],
            "answer": "B"
        },

        # LESSON 14: FOR LOOPS

        {
            "question": "What is a for loop used for?",
            "options": ["A. Repeating code over a sequence", "B. Defining a class", "C. Creating comments", "D. Converting strings"],
            "answer": "A"
        },
        {
            "question": "Which function is commonly used to generate a sequence of numbers?",
            "options": ["A. len()", "B. range()", "C. input()", "D. type()"],
            "answer": "B"
        },
        {
            "question": "How many numbers are generated by range(5)?",
            "options": ["A. 4", "B. 5", "C. 6", "D. 10"],
            "answer": "B"
        },
        {
            "question": "What does range(1, 5) generate?",
            "options": ["A. 1, 2, 3, 4", "B. 1, 2, 3, 4, 5", "C. 0, 1, 2, 3, 4", "D. 2, 3, 4, 5"],
            "answer": "A"
        },
        {
            "question": "Which keyword introduces a for loop?",
            "options": ["A. repeat", "B. loop", "C. for", "D. while"],
            "answer": "C"
        },
        {
            "question": "Can a for loop iterate through a string?",
            "options": ["A. Yes", "B. No", "C. Only if it is empty", "D. Only with an if statement"],
            "answer": "A"
        },
        {
            "question": "What does range(2, 10, 2) generate?",
            "options": ["A. 2, 4, 6, 8", "B. 2, 3, 4, 5", "C. 2, 4, 6, 8, 10", "D. 1, 3, 5, 7"],
            "answer": "A"
        },

        # LESSON 15: WHILE LOOPS

        {
            "question": "When does a while loop continue running?",
            "options": ["A. While its condition is True", "B. Only once", "C. When its condition is False", "D. When the program closes"],
            "answer": "A"
        },
        {
            "question": "What is an infinite loop?",
            "options": ["A. A loop that never starts", "B. A loop that does not stop on its own", "C. A loop that runs once", "D. A loop without code"],
            "answer": "B"
        },
        {
            "question": "What can prevent an unintended infinite while loop?",
            "options": ["A. Updating the loop condition", "B. Removing all variables", "C. Adding comments only", "D. Printing a message"],
            "answer": "A"
        },
        {
            "question": "Which keyword starts a while loop?",
            "options": ["A. for", "B. def", "C. while", "D. if"],
            "answer": "C"
        },
        {
            "question": "What happens if a while condition is initially False?",
            "options": ["A. The loop runs forever", "B. The loop body does not execute", "C. Python crashes", "D. The loop runs twice"],
            "answer": "B"
        },
        {
            "question": "Which loop is useful when the number of repetitions is not known in advance?",
            "options": ["A. while loop", "B. A comment", "C. A variable", "D. A string"],
            "answer": "A"
        },
        {
            "question": "What should a while loop usually do to eventually finish?",
            "options": ["A. Keep the condition unchanged", "B. Update something that affects its condition", "C. Remove its indentation", "D. Delete its keyword"],
            "answer": "B"
        },

        # LESSON 16: BREAK AND CONTINUE

        {
            "question": "What does the break statement do?",
            "options": ["A. Skips one iteration", "B. Exits the current loop", "C. Starts a new loop", "D. Defines a function"],
            "answer": "B"
        },
        {
            "question": "What does continue do inside a loop?",
            "options": ["A. Ends the entire program", "B. Skips to the next iteration", "C. Deletes the loop", "D. Restarts Python"],
            "answer": "B"
        },
        {
            "question": "Which statement completely exits a loop?",
            "options": ["A. continue", "B. break", "C. print", "D. pass"],
            "answer": "B"
        },
        {
            "question": "Which statement skips the remaining code in the current iteration?",
            "options": ["A. break", "B. return", "C. continue", "D. input"],
            "answer": "C"
        },
        {
            "question": "Can break be used inside a for loop?",
            "options": ["A. Yes", "B. No", "C. Only in functions", "D. Only in strings"],
            "answer": "A"
        },
        {
            "question": "Can continue be used inside a while loop?",
            "options": ["A. No", "B. Yes", "C. Only once", "D. Only outside a loop"],
            "answer": "B"
        },
        {
            "question": "What happens when break executes inside a loop?",
            "options": ["A. The current loop terminates", "B. The current iteration repeats", "C. The loop skips one item", "D. The loop condition becomes True"],
            "answer": "A"
        },

        # LESSON 17: NESTED LOOPS

        {
            "question": "What is a nested loop?",
            "options": ["A. A loop inside another loop", "B. A loop without a condition", "C. A variable inside a string", "D. A function without parameters"],
            "answer": "A"
        },
        {
            "question": "Which loop is called the inner loop?",
            "options": ["A. The loop outside another loop", "B. The loop inside another loop", "C. The first function", "D. The last variable"],
            "answer": "B"
        },
        {
            "question": "How many times does the inner loop run if the outer loop runs 3 times and the inner loop runs 2 times per outer iteration?",
            "options": ["A. 2", "B. 3", "C. 5", "D. 6"],
            "answer": "D"
        },
        {
            "question": "Which task can nested loops help perform?",
            "options": ["A. Working with rows and columns", "B. Defining only strings", "C. Installing Python", "D. Creating comments"],
            "answer": "A"
        },
        {
            "question": "Can a for loop contain another for loop?",
            "options": ["A. Yes", "B. No", "C. Only outside a function", "D. Only once in Python"],
            "answer": "A"
        },
        {
            "question": "What is commonly used to represent a grid of rows and columns?",
            "options": ["A. Nested loops", "B. A single comment", "C. A Boolean value", "D. A string method"],
            "answer": "A"
        },
        {
            "question": "In nested loops, how many times does the inner loop normally complete for each outer iteration?",
            "options": ["A. Once only", "B. Its full iteration sequence", "C. Never", "D. Only when the outer loop ends"],
            "answer": "B"
        },

        # LESSON 18: LISTS

        {
            "question": "Which brackets are used to create a list?",
            "options": ["A. ()", "B. {}", "C. []", "D. <>"],
            "answer": "C"
        },
        {
            "question": "Are Python lists ordered?",
            "options": ["A. Yes", "B. No", "C. Only when empty", "D. Only with numbers"],
            "answer": "A"
        },
        {
            "question": "Which method adds an item to the end of a list?",
            "options": ["A. remove()", "B. append()", "C. clear()", "D. pop()"],
            "answer": "B"
        },
        {
            "question": "What is the index of the first item in a Python list?",
            "options": ["A. 1", "B. -1", "C. 0", "D. 2"],
            "answer": "C"
        },
        {
            "question": "Which method removes a specific value from a list?",
            "options": ["A. append()", "B. remove()", "C. insert()", "D. sort()"],
            "answer": "B"
        },
        {
            "question": "Which function returns the number of items in a list?",
            "options": ["A. type()", "B. input()", "C. len()", "D. str()"],
            "answer": "C"
        },
        {
            "question": "What does list[0] access?",
            "options": ["A. The first item", "B. The second item", "C. The last item", "D. The entire list"],
            "answer": "A"
        },

        # LESSON 19: TUPLES

        {
            "question": "Which brackets are commonly used to create a tuple?",
            "options": ["A. []", "B. {}", "C. ()", "D. <>"],
            "answer": "C"
        },
        {
            "question": "Are tuples mutable?",
            "options": ["A. Yes", "B. No", "C. Only with strings", "D. Only with numbers"],
            "answer": "B"
        },
        {
            "question": "What does immutable mean?",
            "options": ["A. Can be changed anytime", "B. Cannot be changed after creation", "C. Contains only numbers", "D. Has no values"],
            "answer": "B"
        },
        {
            "question": "Which method counts how many times a value appears in a tuple?",
            "options": ["A. append()", "B. count()", "C. remove()", "D. add()"],
            "answer": "B"
        },
        {
            "question": "How do you create a tuple containing one item?",
            "options": ["A. (5)", "B. [5]", "C. (5,)", "D. {5}"],
            "answer": "C"
        },
        {
            "question": "Can a tuple contain different data types?",
            "options": ["A. Yes", "B. No", "C. Only integers", "D. Only strings"],
            "answer": "A"
        },
        {
            "question": "Which statement correctly describes a tuple?",
            "options": ["A. It is mutable and unordered", "B. It is ordered and immutable", "C. It stores only strings", "D. It cannot contain numbers"],
            "answer": "B"
        },

        # LESSON 20: SETS

        {
            "question": "Which brackets are used to create a set literal?",
            "options": ["A. []", "B. ()", "C. {}", "D. <>"],
            "answer": "C"
        },
        {
            "question": "What is a major feature of Python sets?",
            "options": ["A. They allow duplicate elements", "B. They store unique elements", "C. They use numeric indexes", "D. They are always sorted"],
            "answer": "B"
        },
        {
            "question": "Which method adds an item to a set?",
            "options": ["A. append()", "B. insert()", "C. add()", "D. update_one()"],
            "answer": "C"
        },
        {
            "question": "Which method removes an item from a set and raises an error if it is missing?",
            "options": ["A. discard()", "B. remove()", "C. clear()", "D. popitem()"],
            "answer": "B"
        },
        {
            "question": "Which operation combines elements from two sets?",
            "options": ["A. Union", "B. Intersection", "C. Difference", "D. Indexing"],
            "answer": "A"
        },
        {
            "question": "Which operation returns elements shared by two sets?",
            "options": ["A. Union", "B. Intersection", "C. Difference", "D. Sorting"],
            "answer": "B"
        },
        {
            "question": "How can you create an empty set?",
            "options": ["A. {}", "B. []", "C. set()", "D. ()"],
            "answer": "C"
        },

        # LESSON 21: DICTIONARIES

        {
            "question": "What does a Python dictionary store?",
            "options": ["A. Only numbers", "B. Key-value pairs", "C. Only strings", "D. Duplicate indexes"],
            "answer": "B"
        },
        {
            "question": "Which brackets are used to create a dictionary?",
            "options": ["A. []", "B. ()", "C. {}", "D. <>"],
            "answer": "C"
        },
        {
            "question": "How do you access a dictionary value using its key?",
            "options": ["A. dictionary.key()", "B. dictionary[key]", "C. dictionary(key)", "D. dictionary->key"],
            "answer": "B"
        },
        {
            "question": "Which method returns all dictionary keys?",
            "options": ["A. values()", "B. items()", "C. keys()", "D. getall()"],
            "answer": "C"
        },
        {
            "question": "Which method returns all dictionary values?",
            "options": ["A. keys()", "B. values()", "C. items()", "D. append()"],
            "answer": "B"
        },
        {
            "question": "Which method safely retrieves a value without raising a KeyError when the key is missing?",
            "options": ["A. get()", "B. popitem()", "C. clear()", "D. sort()"],
            "answer": "A"
        },
        {
            "question": "Can dictionary values be changed after creation?",
            "options": ["A. No", "B. Yes", "C. Only once", "D. Only if they are strings"],
            "answer": "B"
        },

        # LESSON 22: FUNCTIONS

        {
            "question": "Which keyword defines a function in Python?",
            "options": ["A. function", "B. def", "C. create", "D. return"],
            "answer": "B"
        },
        {
            "question": "What is a function?",
            "options": ["A. A reusable block of code", "B. A type of string", "C. A comment", "D. A comparison operator"],
            "answer": "A"
        },
        {
            "question": "How do you call a function named welcome?",
            "options": ["A. call welcome", "B. welcome[]", "C. welcome()", "D. def welcome"],
            "answer": "C"
        },
        {
            "question": "What is a parameter?",
            "options": ["A. A value supplied when calling a function", "B. A variable listed in a function definition", "C. A loop condition", "D. A printed message"],
            "answer": "B"
        },
        {
            "question": "What is an argument?",
            "options": ["A. A value passed to a function when it is called", "B. A function name only", "C. A comment", "D. A return keyword"],
            "answer": "A"
        },
        {
            "question": "Which keyword sends a value back from a function?",
            "options": ["A. print", "B. input", "C. return", "D. def"],
            "answer": "C"
        },
        {
            "question": "What happens when a function reaches the end without a return statement?",
            "options": ["A. It returns 0", "B. It returns None", "C. It returns False", "D. It raises a SyntaxError"],
            "answer": "B"
        },

        # LESSON 23: LIST COMPREHENSIONS

        {
            "question": "What is a list comprehension used for?",
            "options": ["A. Creating lists using a compact expression", "B. Creating functions only", "C. Defining classes", "D. Removing Python"],
            "answer": "A"
        },
        {
            "question": "Which brackets are used in a list comprehension?",
            "options": ["A. {}", "B. ()", "C. []", "D. <>"],
            "answer": "C"
        },
        {
            "question": "Which keyword is commonly used inside a list comprehension to iterate over items?",
            "options": ["A. while", "B. for", "C. def", "D. return"],
            "answer": "B"
        },
        {
            "question": "What does [x * 2 for x in [1, 2, 3]] produce?",
            "options": ["A. [1, 2, 3]", "B. [2, 4, 6]", "C. [1, 4, 9]", "D. [3, 6, 9]"],
            "answer": "B"
        },
        {
            "question": "Can a list comprehension include an if condition?",
            "options": ["A. Yes", "B. No", "C. Only with strings", "D. Only with tuples"],
            "answer": "A"
        },
        {
            "question": "What does [x for x in range(5) if x > 2] produce?",
            "options": ["A. [0, 1, 2]", "B. [2, 3, 4]", "C. [3, 4]", "D. [0, 1, 2, 3, 4]"],
            "answer": "C"
        }

    ]

    score = 0

    for number, question in enumerate(questions, start=1):
        print(f"\nQuestion {number}: {question['question']}")

        for option in question["options"]:
            print(option)

        answer = input("Your answer (A-D): ").strip().upper()

        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
            print("Correct answer:", question["answer"])

    print("\n========== QUIZ RESULT ==========")
    print("Your score:", score, "out of", len(questions))


def view_progress():
    print("\n========== LEARNING PROGRESS ==========")

    total_lessons = 23
    completed_lessons = 0
    remaining_lessons = total_lessons - completed_lessons

    print("Total lessons:", total_lessons)
    print("Completed lessons:", completed_lessons)
    print("Remaining lessons:", remaining_lessons) 
  

display_menu()    
