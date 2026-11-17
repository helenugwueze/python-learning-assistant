def display_lesson_16():
    print("""
LESSON 16: BREAK AND CONTINUE STATEMENTS IN PYTHON

1. INTRODUCTION

Sometimes, programmers need to control how loops behave.

For example:
- Stopping a loop when a particular condition is met.
- Skipping a particular item during a loop.
- Ending a loop before it finishes normally.

Python provides `break` and `continue` statements to control loops.

2. DEFINITION

The `break` and `continue` statements are control statements used to change the normal execution of a loop.

- `break` stops the loop completely.
- `continue` skips the current repetition and moves to the next one.

3. EXPLANATION

A. The Break Statement

The `break` statement immediately stops a loop when a particular condition is met.

Example:

```python
for number in range(1, 6):
    if number == 3:
        break
    print(number)
```

Output:

```text
1
2
```

Explanation:

- The loop starts counting from 1.
- When the number becomes 3, the condition is True.
- The `break` statement stops the loop.
- Numbers 4 and 5 are not printed.

B. The Continue Statement

The `continue` statement skips the current repetition and moves to the next one.

Example:

```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
```

Output:

```text
1
2
4
5
```

Explanation:

- The loop counts from 1 to 5.
- When the number becomes 3, `continue` skips that repetition.
- The loop continues with number 4.

4. EXAMPLES

Example 1: Stopping a Loop

```python
for number in range(1, 11):
    if number == 5:
        break
    print(number)
```

Output:

```text
1
2
3
4
```

Example 2: Skipping a Number

```python
for number in range(1, 6):
    if number == 2:
        continue
    print(number)
```

Output:

```text
1
3
4
5
```

Example 3: Using Break With a While Loop

```python
count = 1

while count <= 5:
    if count == 4:
        break
    print(count)
    count += 1
```

Output:

```text
1
2
3
```

5. SUMMARY

In this lesson, we learned that:

- `break` stops a loop immediately.
- `continue` skips the current repetition.
- Both statements help control how loops execute.
- They can be used with both `for` and `while` loops.

Break and continue statements help programmers control loops more effectively.
    """)