def display_lesson_21():
    print("""
     LESSON 21: DICTIONARIES IN PYTHON

     1. INTRODUCTION

    Python provides different data structures for storing information.

    One of these data structures is called a dictionary.

    Dictionaries allow us to store information using keys and their corresponding values.

    They are useful when working with information such as student records, user accounts, and product details.

    2. DEFINITION

    A dictionary is a collection used to store data in key-value pairs.

    A dictionary has the following features:

    - Ordered: Items maintain their insertion order.
    - Changeable: We can add, update, and remove items.
    - No duplicate keys: Each key must be unique.
    - Key-value pairs: Every key is connected to a value.

    Dictionaries are created using curly brackets {}.

    Example:

    student = {
        "name": "Helen",
        "age": 25,
        "country": "Nigeria"
    }

     3. EXPLANATION

    A. Creating a Dictionary

    We create a dictionary using curly brackets.

    Example:

    student = {
        "name": "Helen",
        "age": 25,
        "course": "Python"
    }

    print(student)

    Output:

    {'name': 'Helen', 'age': 25, 'course': 'Python'}

    B. Accessing Dictionary Values

    We use the key to access its corresponding value.

    Example:

    student = {
        "name": "Helen",
        "age": 25
    }

    print(student["name"])

    Output:

    Helen

     C. Using the get() Method

    We can also use get() to access a dictionary value.

    Example:

    student = {
        "name": "Helen",
        "age": 25
    }

    print(student.get("age"))

    Output:

    25

    The get() method returns None if the key does not exist, unless a default value is provided.

     D. Adding Items to a Dictionary

    We can add a new key-value pair by assigning a value to a new key.

    Example:

    student = {
        "name": "Helen",
        "age": 25
    }

    student["course"] = "Python"

    print(student)

     E. Updating Dictionary Values

    We can change an existing value by assigning a new value to its key.

    Example:

    student = {
        "name": "Helen",
        "age": 25
    }

    student["age"] = 26

    print(student)

    Output:

    {'name': 'Helen', 'age': 26}

     F. Removing Items from a Dictionary

    We use pop() to remove an item using its key.

    Example:

    student = {
        "name": "Helen",
        "age": 25
    }

    student.pop("age")

    print(student)

    Output:

    {'name': 'Helen'}

     G. Getting All Dictionary Keys

    We use keys() to get all the keys in a dictionary.

    Example:

    student = {
        "name": "Helen",
        "age": 25
    }

    print(student.keys())

     H. Getting All Dictionary Values

    We use values() to get all the values in a dictionary.

    Example:

    student = {
        "name": "Helen",
        "age": 25
    }

    print(student.values())

     I. Getting All Dictionary Items

    We use items() to get all key-value pairs.

    Example:

    student = {
        "name": "Helen",
        "age": 25
    }

    print(student.items())

     J. Looping Through a Dictionary

    We can use a for loop to go through a dictionary.

    Example:

    student = {
        "name": "Helen",
        "age": 25,
        "course": "Python"
    }

    for key, value in student.items():
        print(key, value)

    4. EXAMPLES

    Example 1: Student Information

    student = {
        "name": "Helen",
        "age": 25,
        "school": "Python Academy"
    }

    print("Name:", student["name"])
    print("Age:", student["age"])
    print("School:", student["school"])

    Example 2: Product Information

    product = {
        "name": "Laptop",
        "price": 500000,
        "quantity": 2
    }

    print(product)

     Example 3: Updating Student Information

    student = {
        "name": "Helen",
        "score": 70
    }

    student["score"] = 90

    print(student)

    5. SUMMARY

    In this lesson, we learned that:

    - A dictionary stores information in key-value pairs.
    - Dictionaries use curly brackets {}.
    - Keys are used to access values.
    - We use get() to access values safely.
    - We can add new items to a dictionary.
    - We can update existing values.
    - We use pop() to remove an item.
    - We use keys() to get dictionary keys.
    - We use values() to get dictionary values.
    - We use items() to get key-value pairs.
    - We can loop through dictionaries using a for loop.

    REMEMBER: A dictionary stores information using keys and their corresponding values.
    """)