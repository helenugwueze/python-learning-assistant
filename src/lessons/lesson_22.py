def display_lesson_22():
    print("""
    LESSON 22: FUNCTIONS IN PYTHON

1. INTRODUCTION

When writing Python programs, we sometimes need to perform the same task several times.

For example, a program may need to:
- Welcome a user.
- Calculate numbers.
- Check whether a number is even or odd.
- Display information.
- Perform calculations.

Instead of writing the same instructions repeatedly, Python allows us to create functions.

Functions help us organize our programs into smaller and manageable sections.

They also make our code easier to read, understand, test, and maintain.

2. DEFINITION

A function is a reusable block of code designed to perform a particular task.

A function only runs when it is called.

We create functions using the def keyword.

The basic structure of a function is:

def function_name():
    statement

Explanation:

- def: Tells Python that we are creating a function.
- function_name: The name given to the function.
- Parentheses (): Used to hold parameters.
- Colon (:): Marks the beginning of the function body.
- Indentation: Shows which instructions belong to the function.

3. EXPLANATION

A. Creating a Function

We use the def keyword to create a function.

Example:

def greet():
    print("Hello, welcome to Python!")

Explanation:

- def creates the function.
- greet is the function name.
- The print statement is the instruction the function performs.

B. Calling a Function

Creating a function does not automatically execute its instructions.

We must call the function.

Example:

def greet():
    print("Hello, welcome to Python!")

greet()

Output:

Hello, welcome to Python!

Explanation:

When Python reaches greet(), it executes the instructions inside the function.

C. Functions with Parameters

A parameter is a variable written inside the parentheses of a function definition.

Parameters allow us to pass information into functions.

Example:

def greet(name):
    print("Hello", name)

greet("Helen")

Output:

Hello Helen

Explanation:

- name is the parameter.
- "Helen" is the argument.
- The function receives the argument and uses it in the print statement.

D. Functions with Multiple Parameters

A function can accept more than one parameter.

Example:

def add_numbers(first_number, second_number):
    print(first_number + second_number)

add_numbers(10, 5)

Output:

15

Explanation:

- first_number receives 10.
- second_number receives 5.
- Python adds both values and displays the result.

E. Understanding Arguments

An argument is the actual value passed to a function when we call it.

Example:

def greet(name):
    print("Welcome", name)

greet("Helen")

Explanation:

- name is the parameter.
- "Helen" is the argument.

Parameters are defined when creating a function, while arguments are supplied when calling it.

F. The return Statement

The return statement sends a result back from a function.

It allows us to store and use the result somewhere else in our program.

Example:

def add_numbers(a, b):
    return a + b

result = add_numbers(10, 5)

print(result)

Output:

15

Explanation:

- The function receives two numbers.
- Python adds the numbers.
- return sends the answer back.
- The result is stored in the result variable.

G. Difference Between print() and return

print() displays information on the screen.

return sends a result back to the part of the program that called the function.

Example using print():

def multiply(a, b):
    print(a * b)

multiply(4, 5)

Output:

20

Example using return:

def multiply(a, b):
    return a * b

answer = multiply(4, 5)

print(answer)

Output:

20

H. Functions with Default Parameters

A default parameter is a parameter that already has a value.

Python uses that value when the caller does not provide an argument.

Example:

def greet(name="Guest"):
    print("Hello", name)

greet()

Output:

Hello Guest

We can also provide another argument.

Example:

greet("Helen")

Output:

Hello Helen

I. Returning Multiple Values

A Python function can return more than one value.

Example:

def calculate(a, b):
    return a + b, a - b

addition, subtraction = calculate(10, 5)

print(addition)
print(subtraction)

Output:

15
5

J. Using Functions with Conditions

We can place conditional statements inside functions.

Example:

def check_number(number):
    if number > 0:
        print("Positive number")
    elif number < 0:
        print("Negative number")
    else:
        print("Zero")

check_number(10)

Output:

Positive number

K. Using Functions with Loops

Functions can also contain loops.

Example:

def count_numbers():
    for number in range(1, 6):
        print(number)

count_numbers()

Output:

1
2
3
4
5

L. Why Functions Are Important

Functions are important because they:

- Reduce repeated code.
- Make programs easier to organize.
- Improve code readability.
- Make debugging easier.
- Allow us to reuse instructions.
- Divide large programs into smaller tasks.

4. EXAMPLES

Example 1: Welcome Function

def welcome():
    print("Welcome to Python Learning Assistant!")
    print("Start learning Python today.")

welcome()

Output:

Welcome to Python Learning Assistant!
Start learning Python today.

Example 2: Addition Function

def add_numbers(a, b):
    return a + b

answer = add_numbers(20, 10)

print("Answer:", answer)

Output:

Answer: 30

Example 3: Even or Odd Function

def check_even(number):
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

check_even(8)

Output:

Even number

Example 4: Student Information Function

def student_information(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

student_information("Helen", 25, "Python")

Output:

Name: Helen
Age: 25
Course: Python

Example 5: Area of a Rectangle

def calculate_area(length, width):
    return length * width

area = calculate_area(10, 5)

print("Area:", area)

Output:

Area: 50

5. SUMMARY

In this lesson, we learned that:

- A function is a reusable block of code.
- We create functions using the def keyword.
- A function runs when it is called.
- Parameters allow functions to receive information.
- Arguments are the actual values passed to functions.
- A function can accept multiple parameters.
- The return statement sends a result back.
- print() displays information on the screen.
- Default parameters provide values when arguments are not supplied.
- Functions can return multiple values.
- Functions can contain conditions and loops.
- Functions help us organize and reuse code.

REMEMBER:

Functions allow us to write code once and reuse it whenever we need it.
    """)
