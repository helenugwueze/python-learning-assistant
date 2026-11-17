def display_lesson_12():
    print("""
LESSON 12: COMPARISON OPERATORS IN PYTHON

1. INTRODUCTION

In Python, programmers sometimes need to compare two values to make decisions.

For example:
- Checking whether someone is older than 18.
- Checking whether two numbers are equal.
- Checking whether a student's score is greater than or equal to 50.

Python uses comparison operators to perform these comparisons.

2. DEFINITION

Comparison operators are symbols used to compare two values. They return a Boolean result, which is either True or False.

3. EXPLANATION

Python has six main comparison operators.

A. Equal to (==)

Checks whether two values are equal.

Example:

```python
print(10 == 10)
```

Output:

```text
True
```

B. Not Equal to (!=)

Checks whether two values are different.

Example:

```python
print(10 != 5)
```

Output:

```text
True
```

C. Greater Than (>)

Checks whether the left value is greater than the right value.

Example:

```python
print(10 > 5)
```

Output:

```text
True
```

D. Less Than (<)

Checks whether the left value is smaller than the right value.

Example:

```python
print(5 < 10)
```

Output:

```text
True
```

E. Greater Than or Equal to (>=)

Checks whether a value is greater than or equal to another value.

Example:

```python
print(10 >= 10)
```

Output:

```text
True
```

F. Less Than or Equal to (<=)

Checks whether a value is less than or equal to another value.

Example:

```python
print(5 <= 10)
```

Output:

```text
True
```

4. EXAMPLES

Example 1: Comparing Numbers

```python
first_number = 20
second_number = 10

print(first_number > second_number)
print(first_number == second_number)
print(first_number != second_number)
```

Output:

```text
True
False
True
```

Example 2: Checking Student Scores

```python
score = 65

print(score >= 50)
```

Output:

```text
True
```

Example 3: Checking Age

```python
age = 16

print(age >= 18)
```

Output:

```text
False
```

5. SUMMARY

In this lesson, we learned that:

- Comparison operators compare two values.
- `==` checks whether values are equal.
- `!=` checks whether values are different.
- `>` checks whether a value is greater.
- `<` checks whether a value is smaller.
- `>=` checks whether a value is greater than or equal to another.
- `<=` checks whether a value is less than or equal to another.
- Comparison operators return True or False.

Comparison operators help Python programs make decisions based on values.
    """)
