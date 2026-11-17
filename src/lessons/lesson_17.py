def display_lesson_17():
    print("""
LESSON 17: NESTED LOOPS IN PYTHON

1. INTRODUCTION

Sometimes, programmers need to use one loop inside another loop to perform repeated tasks.

For example:
- Displaying rows and columns of numbers.
- Creating multiplication tables.
- Printing patterns using stars.
- Working with lists that contain other lists.

Python allows programmers to place one loop inside another. This is called a nested loop.

2. DEFINITION

A nested loop is a loop placed inside another loop. The inner loop executes completely for every repetition of the outer loop.

3. EXPLANATION

A. Basic Nested Loop

Example:

```python
for number in range(1, 4):
    for value in range(1, 3):
        print(number, value)
```

Output:

```text
1 1
1 2
2 1
2 2
3 1
3 2
```

Explanation:

- The outer loop runs three times.
- The inner loop runs two times for every outer loop repetition.
- The inner loop completes before the outer loop moves to its next repetition.

B. Nested Loops With Numbers

Example:

```python
for row in range(1, 4):
    for column in range(1, 4):
        print(column, end=" ")
    print()
```

Output:

```text
1 2 3
1 2 3
1 2 3
```

Explanation:

- The outer loop controls the rows.
- The inner loop controls the columns.
- `end=" "` keeps the numbers on the same line.
- `print()` moves to the next line after each row.

4. EXAMPLES

Example 1: Printing Stars

```python
for row in range(3):
    for column in range(4):
        print("*", end=" ")
    print()
```

Output:

```text
* * * *
* * * *
* * * *
```

Example 2: Multiplication Table

```python
for number in range(1, 4):
    for value in range(1, 4):
        print(number * value, end=" ")
    print()
```

Output:

```text
1 2 3
2 4 6
3 6 9
```

Example 3: Printing Number Patterns

```python
for row in range(1, 5):
    for column in range(row):
        print(row, end=" ")
    print()
```

Output:

```text
1
2 2
3 3 3
4 4 4 4
```

5. SUMMARY

In this lesson, we learned that:

- A nested loop is a loop inside another loop.
- The outer loop controls the main repetitions.
- The inner loop completes its repetitions for every outer loop repetition.
- Nested loops can be used to create patterns and multiplication tables.
- Nested loops help solve problems that involve rows and columns.

Nested loops are useful when a program needs to repeat tasks within other repeated tasks.
    """)