def display_lesson_20():
    print("""
  # LESSON 20: SETS IN PYTHON

## 1. INTRODUCTION

Python has different data structures for storing multiple values.

One of these data structures is called a set.

Sets allow us to store multiple items in one variable. They are useful when we want to keep unique values and remove duplicates.

In this lesson, we will learn how to create sets, access their items, add and remove items, and use set methods.

## 2. DEFINITION

A set is a collection used to store multiple unique items in a single variable.

A set has the following features:

- Unordered: Items do not have a fixed position.
- Unchangeable items: Individual items cannot be modified, but items can be added or removed.
- No duplicates: A set does not allow repeated values.
- Different data types: A set can contain strings, numbers, and other supported data types.

Sets are created using curly brackets `{}`.

Example:

```python
fruits = {"apple", "banana", "orange"}
```

## 3. EXPLANATION

### Creating a Set

We create a set by placing items inside curly brackets.

Example:

```python
fruits = {"apple", "banana", "orange"}

print(fruits)
```

Output (the order may differ):

```text
{'apple', 'banana', 'orange'}
```

### Duplicate Values in Sets

Sets automatically remove duplicate values.

Example:

```python
numbers = {10, 20, 10, 30, 20}

print(numbers)
```

Output (the order may differ):

```text
{10, 20, 30}
```

### Accessing Set Items

Sets are unordered, so we cannot access their items using index numbers.

Instead, we can use a `for` loop to go through the items.

Example:

```python
fruits = {"apple", "banana", "orange"}

for fruit in fruits:
    print(fruit)
```

### Adding Items to a Set

We use the `add()` method to add one item to a set.

Example:

```python
fruits = {"apple", "banana"}

fruits.add("orange")

print(fruits)
```

### Adding Multiple Items

We use the `update()` method to add multiple items.

Example:

```python
fruits = {"apple", "banana"}

fruits.update(["orange", "mango"])

print(fruits)
```

### Removing Items from a Set

We use the `remove()` method to remove an item.

Example:

```python
fruits = {"apple", "banana", "orange"}

fruits.remove("banana")

print(fruits)
```

Note: `remove()` produces an error if the item does not exist.

We can also use `discard()`, which does not produce an error if the item is missing.

Example:

```python
fruits = {"apple", "banana"}

fruits.discard("orange")

print(fruits)
```

### Finding the Length of a Set

We use `len()` to count the number of items.

Example:

```python
numbers = {10, 20, 30, 40}

print(len(numbers))
```

Output:

```text
4
```

### Checking if an Item Exists

We use the `in` keyword to check whether an item exists in a set.

Example:

```python
fruits = {"apple", "banana", "orange"}

print("apple" in fruits)
```

Output:

```text
True
```

### Clearing a Set

We use the `clear()` method to remove all items from a set.

Example:

```python
fruits = {"apple", "banana", "orange"}

fruits.clear()

print(fruits)
```

Output:

```text
set()
```

## 4. EXAMPLES

### Example 1: Student Names

```python
students = {"Helen", "John", "Mary"}

for student in students:
    print(student)
```

### Example 2: Removing Duplicate Numbers

```python
numbers = {1, 2, 2, 3, 3, 4}

print(numbers)
```

Output (the order may differ):

```text
{1, 2, 3, 4}
```

### Example 3: Checking Available Colors

```python
colors = {"red", "blue", "green"}

if "blue" in colors:
    print("Blue is available")
```

Output:

```text
Blue is available
```

## 5. SUMMARY

In this lesson, we learned that:

- A set stores multiple items in one variable.
- Sets are created using curly brackets `{}`.
- Sets do not allow duplicate values.
- Sets are unordered.
- We use `add()` to add one item.
- We use `update()` to add multiple items.
- We use `remove()` and `discard()` to remove items.
- We use `len()` to count items.
- We use `clear()` to remove all items.
- We use loops to go through set items.

**Remember:** Sets are useful when you want to store unique values without duplicates.
    """)