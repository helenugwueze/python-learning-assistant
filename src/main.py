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
        "10": "Comments"
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


    elif topic_choice in topics:
        print("topic:", topic[topic_choice])
            
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
            print("take a quiz")
           
        elif choice == "3":
            print("view progress")
           
        elif choice == "4":
            print("Goodbye")
           
        else:
            print("Invalid choice. Please select 1-4.")   
           


display_menu()