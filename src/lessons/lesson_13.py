def display_lesson_13():
    print("""
    LESSON 13: LOGICAL OPERATORS IN PYTHON

1. INTRODUCTION

In Python, programmers sometimes need to check more than one condition before making a decision.

For example:
- A student must pass Mathematics AND English to qualify for admission.
- A person can enter if they have a valid ticket OR an invitation.
- A user cannot continue if they are NOT logged in.

Python uses logical operators to combine conditions and make decisions.

2. DEFINITION

Logical operators are operators used to combine two or more conditions and return a Boolean result, which is either True or False.

3. EXPLANATION

Python has three main logical operators:

A. AND Operator

The `and` operator returns True only when both conditions are True.

Example:

```python
age = 20
has_id = True

print(age >= 18 and has_id == True)
```

Output:

```text
True
```

Explanation:

- `age >= 18` checks whether the person is at least 18.
- `has_id == True` checks whether the person has an ID.
- Both conditions are True, so the result is True.

B. OR Operator

The `or` operator returns True when at least one condition is True.

Example:

```python
has_ticket = True
has_invitation = False

print(has_ticket or has_invitation)
```

Output:

```text
True
```

Explanation:

The first condition is True, so the result is True even though the second condition is False.

C. NOT Operator

The `not` operator reverses a Boolean result.

Example:

```python
is_raining = False

print(not is_raining)
```

Output:

```text
True
```

Explanation:

The original value is False. The `not` operator reverses it to True.

4. EXAMPLES

Example 1: Checking Admission Requirements

```python
math_score = 70
english_score = 65

if math_score >= 50 and english_score >= 50:
    print("You qualify for admission.")
else:
    print("You do not qualify.")
```

Output:

```text
You qualify for admission.
```

Example 2: Checking Access

```python
has_ticket = False
has_invitation = True

if has_ticket or has_invitation:
    print("Access granted.")
else:
    print("Access denied.")
```

Output:

```text
Access granted.
```

Example 3: Checking Login Status

```python
is_logged_in = False

if not is_logged_in:
    print("Please log in.")
else:
    print("Welcome back!")
```

Output:

```text
Please log in.
```

5. SUMMARY

In this lesson, we learned that:

- Logical operators combine conditions.
- `and` returns True when both conditions are True.
- `or` returns True when at least one condition is True.
- `not` reverses a Boolean result.
- Logical operators help Python make decisions using multiple conditions.

Logical operators are useful when building programs that need to check several conditions before performing an action.
    """)

