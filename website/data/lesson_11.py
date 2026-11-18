def display_lesson_11():
    print("""# LESSON 11: CONDITIONAL STATEMENTS IN PYTHON

 1. INTRODUCTION

Python programs sometimes need to make decisions.

For example:
- If a student passes an exam, display "Congratulations".
- If a person is 18 or older, allow them to register.
- If it is raining, carry an umbrella.

Python uses conditional statements to make these decisions.

2. DEFINITION

Conditional statements are instructions that allow Python to make decisions based on whether a condition is True or False.

3. EXPLANATION

Python provides different types of conditional statements:

A. The if Statement

The `if` statement executes a block of code when a condition is True.

Example:

```python
age = 20

if age >= 18:
    print("You are an adult.")
```

Explanation:

- `age = 20` stores the person's age.
- `if age >= 18` checks whether the age is at least 18.
- `print()` displays the message if the condition is True.

B. The else Statement

The `else` statement executes when the if condition is False.

Example:

```python
age = 15

if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")
```

Explanation:

Python checks whether the age is at least 18.

Since the age is 15, the condition is False, so Python executes the else block.

C. The elif Statement

The `elif` statement means "else if".

It allows Python to check additional conditions when the previous condition is False.

Example:

```python
score = 75

if score >= 80:
    print("Grade A")
elif score >= 60:
    print("Grade B")
else:
    print("Grade C")
```

Explanation:

- Python first checks whether the score is 80 or above.
- If that condition is False, it checks whether the score is 60 or above.
- If both conditions are False, it executes the else block.

The output is:

```text
Grade B
```

4. EXAMPLES

Example 1: Checking a Number

```python
number = 10

if number > 0:
    print("Positive number")
else:
    print("Negative number or zero")
```

Output:

```text
Positive number
```

Example 2: Checking Password Length

```python
password = "python123"

if len(password) >= 8:
    print("Password accepted")
else:
    print("Password is too short")
```

Output:

```text
Password accepted
```

Example 3: Checking Examination Results

```python
score = 45

if score >= 50:
    print("You passed")
else:
    print("You failed")
```

Output:

```text
You failed
```

5. SUMMARY

In this lesson, we learned that:

- Conditional statements help Python make decisions.
- The `if` statement checks a condition.
- The `else` statement runs when the condition is False.
- The `elif` statement checks additional conditions.
- Conditions produce either True or False results.

Conditional statements help programmers create programs that can respond differently depending on the situation.

    """)
