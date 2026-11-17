def display_lesson_18():
    print("""
LESSON 18: LISTS IN PYTHON

1. INTRODUCTION

In Python, programmers sometimes need to store multiple values in one variable instead of creating a separate variable for every value.

For example:
- Storing the names of students in a class.
- Keeping a list of fruits.
- Storing examination scores.
- Managing items in a shopping list.
- Keeping track of products in a store.

Creating separate variables for every item can make a program difficult to manage.

Python solves this problem by providing a data structure called a list.

Lists allow programmers to store, access, modify, add, and remove multiple items in one variable.

2. DEFINITION

A list is a built-in Python data structure used to store multiple items in a single variable.

Lists are:
- Ordered: Items maintain their positions.
- Changeable: Items can be modified.
- Allow duplicates: The same value can appear more than once.
- Able to store different data types.

3. EXPLANATION

A. Creating a List

Lists are created using square brackets `[]`, with items separated by commas.

Example:

```python
fruits = ["apple", "banana", "orange"]

print(fruits)
```

Output:

```text
['apple', 'banana', 'orange']
```

Explanation:

- `fruits` is the name of the variable.
- Square brackets `[]` create the list.
- Each fruit is an item in the list.
- Commas separate the items.

B. Accessing List Items

Each item in a list has an index.

An index represents the position of an item in a list.

Python starts counting indexes from 0.

Example:

```python
fruits = ["apple", "banana", "orange"]

print(fruits[0])
print(fruits[1])
print(fruits[2])
```

Output:

```text
apple
banana
orange
```

Explanation:

- Index `0` represents apple.
- Index `1` represents banana.
- Index `2` represents orange.

C. Negative Indexing

Python also allows programmers to access list items using negative indexes.

Negative indexing starts counting from the end of the list.

Example:

```python
fruits = ["apple", "banana", "orange"]

print(fruits[-1])
print(fruits[-2])
```

Output:

```text
orange
banana
```

Explanation:

- `-1` accesses the last item.
- `-2` accesses the second-to-last item.

D. Changing List Items

Lists are changeable, which means programmers can modify existing items.

Example:

```python
fruits = ["apple", "banana", "orange"]

fruits[1] = "mango"

print(fruits)
```

Output:

```text
['apple', 'mango', 'orange']
```

Explanation:

The item at index 1 was originally banana. We replaced it with mango.

E. Adding Items to a List

Python provides different methods for adding new items to a list.

**1. append()**

The `append()` method adds an item to the end of a list.

Example:

```python
fruits = ["apple", "banana"]

fruits.append("orange")

print(fruits)
```

Output:

```text
['apple', 'banana', 'orange']
```

**2. insert()**

The `insert()` method adds an item at a specific position.

Example:

```python
fruits = ["apple", "orange"]

fruits.insert(1, "banana")

print(fruits)
```

Output:

```text
['apple', 'banana', 'orange']
```

**3. extend()**

The `extend()` method adds multiple items from another collection to an existing list.

Example:

```python
fruits = ["apple", "banana"]

fruits.extend(["orange", "mango"])

print(fruits)
```

Output:

```text
['apple', 'banana', 'orange', 'mango']
```

F. Removing Items From a List

Python provides different methods for removing items.

**1. remove()**

The `remove()` method removes a specific value from a list.

Example:

```python
fruits = ["apple", "banana", "orange"]

fruits.remove("banana")

print(fruits)
```

Output:

```text
['apple', 'orange']
```

**2. pop()**

The `pop()` method removes an item using its index. If no index is provided, it removes the last item.

Example:

```python
fruits = ["apple", "banana", "orange"]

fruits.pop()

print(fruits)
```

Output:

```text
['apple', 'banana']
```

**3. clear()**

The `clear()` method removes all items from a list.

Example:

```python
fruits = ["apple", "banana", "orange"]

fruits.clear()

print(fruits)
```

Output:

```text
[]
```

G. Finding the Number of Items

The `len()` function returns the number of items in a list.

Example:

```python
numbers = [10, 20, 30, 40, 50]

print(len(numbers))
```

Output:

```text
5
```

H. Checking if an Item Exists

The `in` operator checks whether an item exists in a list.

Example:

```python
fruits = ["apple", "banana", "orange"]

print("banana" in fruits)
print("mango" in fruits)
```

Output:

```text
True
False
```

I. Looping Through a List

A `for` loop allows programmers to access and display every item in a list.

Example:

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

Explanation:

Python goes through the list one item at a time and displays each name.

J. Sorting a List

The `sort()` method arranges list items in ascending order by default.

Example:

```python
numbers = [5, 2, 8, 1, 3]

numbers.sort()

print(numbers)
```

Output:

```text
[1, 2, 3, 5, 8]
```

K. Reversing a List

The `reverse()` method reverses the order of items in a list.

Example:

```python
numbers = [1, 2, 3, 4, 5]

numbers.reverse()

print(numbers)
```

Output:

```text
[5, 4, 3, 2, 1]
```

L. Lists With Different Data Types

Python lists can store different types of data in one collection.

Example:

```python
student = ["Helen", 20, 85.5, True]

print(student)
```

Output:

```text
['Helen', 20, 85.5, True]
```

Explanation:

- `"Helen"` is a string.
- `20` is an integer.
- `85.5` is a float.
- `True` is a Boolean value.

4. EXAMPLES

Example 1: Managing Student Names

```python
students = ["Helen", "John", "Mary"]

students.append("David")

for student in students:
    print(student)
```

Output:

```text
Helen
John
Mary
David
```

Example 2: Calculating Total Scores

```python
scores = [70, 80, 65, 90, 75]

total = sum(scores)

print("Total score:", total)
```

Output:

```text
Total score: 380
```

Explanation:

- `scores` stores the students' scores.
- `sum()` adds all the numbers in the list.
- `total` stores the result.
- `print()` displays the total score.

Example 3: Finding the Highest Score

```python
scores = [70, 85, 60, 95, 75]

highest_score = max(scores)

print("Highest score:", highest_score)
```

Output:

```text
Highest score: 95
```

Example 4: Finding the Lowest Score

```python
scores = [70, 85, 60, 95, 75]

lowest_score = min(scores)

print("Lowest score:", lowest_score)
```

Output:

```text
Lowest score: 60
```

Example 5: Creating a Shopping List

```python
shopping_list = ["rice", "beans", "milk"]

shopping_list.append("bread")

shopping_list.remove("beans")

print("My shopping list:", shopping_list)
```

Output:

```text
My shopping list: ['rice', 'milk', 'bread']
```

5. SUMMARY

In this lesson, we learned that:

- A list stores multiple items in one variable.
- Lists are created using square brackets `[]`.
- Lists are ordered and changeable.
- Lists allow duplicate values.
- List indexes start from 0.
- Negative indexing starts from the end.
- `append()` adds an item to the end.
- `insert()` adds an item at a specific position.
- `extend()` adds multiple items.
- `remove()` removes a specific value.
- `pop()` removes an item using its index.
- `clear()` removes all items.
- `len()` counts the number of items.
- `in` checks whether an item exists.
- `sort()` arranges items in ascending order.
- `reverse()` reverses the order of items.
- `sum()` calculates the total of numerical items.
- `max()` finds the highest value.
- `min()` finds the lowest value.
- A `for` loop can access each item in a list.

Lists are important in Python because they allow programmers to store, organise, access, and manage multiple values efficiently.
    """)