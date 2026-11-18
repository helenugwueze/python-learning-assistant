def display_lesson_15():
    print("""
LESSON 15: WHILE LOOPS IN PYTHON

1. INTRODUCTION

Sometimes, programmers need to repeat instructions while a particular condition remains True.

For example:
- Asking a user to enter a password until it is correct.
- Counting numbers while a condition is True.
- Repeating a task until the user decides to stop.

Python uses `while` loops to repeat instructions as long as a condition remains True.

2. DEFINITION

A while loop is a control structure that repeatedly executes a block of code as long as a given condition is True.

3. EXPLANATION

A. Basic While Loop

Example:

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

Output:

```text
1
2
3
4
5
```

Explanation:

- `number = 1` gives the variable its starting value.
- `while number <= 5` checks whether the condition is True.
- `print(number)` displays the current number.
- `number += 1` increases the number by 1.
- The loop stops when the condition becomes False.

B. While Loop With User Input

A while loop can repeat an instruction until the user enters the correct information.

Example:

```python
password = ""

while password != "python123":
    password = input("Enter your password: ")

print("Access granted!")
```

Explanation:

Python keeps asking for the password while it is incorrect. When the correct password is entered, the condition becomes False and the loop stops.

C. Infinite While Loop

An infinite loop is a loop that continues running because its condition never becomes False.

Example:

```python
while True:
    print("Python is interesting!")
```

This loop continues printing the message until it is manually stopped.

4. EXAMPLES

Example 1: Counting Numbers

```python
count = 1

while count <= 10:
    print(count)
    count += 1
```

Output:

```text
1
2
3
4
5
6
7
8
9
10
```

Example 2: Countdown

```python
number = 5

while number >= 1:
    print(number)
    number -= 1

print("Countdown finished!")
```

Output:

```text
5
4
3
2
1
Countdown finished!
```

Example 3: Checking a Number

```python
number = 1

while number < 4:
    print("Number is less than 4")
    number += 1
```

Output:

```text
Number is less than 4
Number is less than 4
Number is less than 4
```

5. SUMMARY

In this lesson, we learned that:

- A while loop repeats instructions while a condition is True.
- The condition is checked before each repetition.
- A variable can be updated inside the loop.
- A while loop stops when its condition becomes False.
- An infinite loop continues running until it is stopped.

While loops are useful when a program needs to repeat an action until a particular condition changes.
    """)
   