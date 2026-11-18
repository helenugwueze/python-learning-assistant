def display_lesson_19():
    print("""
LESSON 19: TUPLES IN PYTHON

1. INTRODUCTION

Python has different data structures used to store multiple values.

One of these data structures is called a tuple.

Tuples allow us to store several items in one variable.

In this lesson, we will learn how to create tuples, access their items, and use tuple methods.

2. DEFINITION

A tuple is a collection used to store multiple items in a single variable.

A tuple is:

- Ordered: Items have a fixed position.
- Unchangeable: Items cannot be modified after creation.
- Allows duplicates: The same value can appear more than once.
- Can store different data types.

Tuples are created using round brackets `()`.

Example:

```python
fruits = ("apple", "banana", "orange")
```

3. EXPLANATION

Creating a Tuple

We create a tuple by placing items inside round brackets.

Example:

```python
fruits = ("apple", "banana", "orange")

print(fruits)
```

Output:

```text
('apple', 'banana', 'orange')
```

Accessing Tuple Items

We use index numbers to access items in a tuple.

Remember: Python indexing starts from 0.

Example:

```python
fruits = ("apple", "banana", "orange")

print(fruits[0])
print(fruits[1])
```

Output:

```text
apple
banana
```

Negative Indexing

Negative indexing allows us to access items from the end of a tuple.

Example:

```python
fruits = ("apple", "banana", "orange")

print(fruits[-1])
```

Output:

```text
orange
```

Tuples Cannot Be Changed

Tuples are unchangeable.

This means we cannot replace an item after creating a tuple.

Example:

```python
fruits = ("apple", "banana", "orange")

fruits[0] = "mango"
```

This will produce an error because tuples do not allow item changes.

Finding the Length of a Tuple

We use `len()` to count the number of items in a tuple.

Example:

```python
numbers = (10, 20, 30, 40)

print(len(numbers))
```

Output:

```text
4
```

Checking if an Item Exists

We use the `in` keyword to check whether an item exists in a tuple.

Example:

```python
fruits = ("apple", "banana", "orange")

print("apple" in fruits)
```

Output:

```text
True
```

Looping Through a Tuple

We can use a `for` loop to access every item in a tuple.

Example:

```python
fruits = ("apple", "banana", "orange")

for fruit in fruits:
    print(fruit)
```

Output:

```text
apple
banana
orange
```

Counting Items in a Tuple

We use the `count()` method to count how many times a value appears.

Example:

```python
numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))
```

Output:

```text
3
```

Finding the Position of an Item

We use the `index()` method to find the position of an item.

Example:

```python
fruits = ("apple", "banana", "orange")

print(fruits.index("banana"))
```

Output:

```text
1
```

4. EXAMPLES

Example 1: Student Information

```python
student = ("Helen", 22, "Python")

print(student)
```

Output:

```text
('Helen', 22, 'Python')
```

Example 2: Numbers in a Tuple

```python
numbers = (5, 10, 15, 20)

print(numbers[2])
```

Output:

```text
15
```

Example 3: Checking for an Item

```python
colors = ("red", "blue", "green")

if "blue" in colors:
    print("Blue is available")
```

Output:

```text
Blue is available
```

5. SUMMARY

In this lesson, we learned that:

- A tuple stores multiple items in one variable.
- Tuples are created using round brackets `()`.
- Tuples are ordered.
- Tuples allow duplicate values.
- Tuples can store different data types.
- Tuples cannot be changed after creation.
- We use indexing to access tuple items.
- We use `len()` to count items.
- We use `count()` to count repeated values.
- We use `index()` to find an item's position.
- We can loop through tuples using a `for` loop.

**Remember:** The major difference between a list and a tuple is that a list can be changed, but a tuple cannot be changed.
    """)
