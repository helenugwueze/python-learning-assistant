def display_lesson_14():
    print("""
LESSON 14: FOR LOOPS IN PYTHON

1. INTRODUCTION

Sometimes, programmers need to repeat an instruction several times.

For example:
- Displaying numbers from 1 to 10.
- Printing the names of students in a list.
- Repeating an action for every item in a collection.

Python uses `for` loops to repeat instructions without writing the same code many times.

2. DEFINITION

A for loop is a control structure that repeats a block of code for each item in a sequence.

3. EXPLANATION

A for loop is commonly used with sequences such as lists, strings, and ranges.

A. Basic For Loop

Example:

```python
for number in range(5):
    print(number)
```

Output:

```text
0
1
2
3
4
```

Explanation:

- `for` starts the loop.
- `number` is the loop variable.
- `range(5)` generates numbers from 0 to 4.
- `print(number)` displays each number.

B. Using Range()

The `range()` function generates a sequence of numbers.

Example:

```python
for number in range(1, 6):
    print(number)
```

Output:

```text
1
2
3
4
5
```

C. Looping Through a String

A for loop can also go through each character in a string.

Example:

```python
name = "Helen"

for letter in name:
    print(letter)
```

Output:

```text
H
e
l
e
n
```

4. EXAMPLES

Example 1: Printing Numbers

```python
for number in range(1, 11):
    print(number)
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

Example 2: Printing Names

```python
names = ["Helen", "John", "Mary"]

for name in names:
    print(name)
```

Output:

```text
Helen
John
Mary
```

Example 3: Multiplication Table

```python
number = 5

for value in range(1, 6):
    print(number, "x", value, "=", number * value)
```

Output:

```text
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
```

5. SUMMARY

In this lesson, we learned that:

- A for loop repeats instructions.
- A for loop works with sequences.
- `range()` generates a sequence of numbers.
- A loop variable stores the current item during each repetition.
- For loops help reduce repeated code.

For loops are useful when a program needs to perform the same action for several items.
    """)