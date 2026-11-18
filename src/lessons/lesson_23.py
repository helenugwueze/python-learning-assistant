def display_lesson_23():
    print("""
    LESSON 23: LIST COMPREHENSIONS IN PYTHON

    1. INTRODUCTION

    In Python, lists allow us to store multiple values in one variable.

    Sometimes, we need to create a new list from an existing list.

    We can use a for loop to achieve this.

    However, Python provides a shorter and cleaner way to create lists.

    This method is called List Comprehension.

    List comprehensions help us write shorter code while creating
    new lists from existing sequences.

    They are useful when working with numbers, names, scores,
    and other collections of data.

    2. DEFINITION

    List comprehension is a shorter way of creating a new list
    using an existing sequence.

    It allows us to combine a loop and an optional condition
    into one expression.

    The basic structure is:

    new_list = [expression for item in sequence]

    Explanation:

    - new_list: The new list we want to create.
    - expression: The value we want to place inside the new list.
    - for: Used to go through each item.
    - item: Represents each value in the sequence.
    - sequence: The collection we want to work with.

    3. EXPLANATION

    A. Creating a List Using a For Loop

    Before understanding list comprehensions, let's see how
    we normally create a new list using a for loop.

    Example:

    numbers = [1, 2, 3, 4, 5]

    squares = []

    for number in numbers:
        squares.append(number * number)

    print(squares)

    Output:

    [1, 4, 9, 16, 25]

    Explanation:

    - numbers stores the original list.
    - squares is an empty list.
    - The for loop goes through each number.
    - append() adds the squared number to the new list.
    - print() displays the result.

    B. Creating the Same List Using List Comprehension

    We can write the previous example in a shorter way.

    Example:

    numbers = [1, 2, 3, 4, 5]

    squares = [number * number for number in numbers]

    print(squares)

    Output:

    [1, 4, 9, 16, 25]

    Explanation:

    - number * number calculates the square.
    - for number in numbers goes through every number.
    - The calculated values are placed inside a new list.

    C. List Comprehension with Numbers

    We can use list comprehensions to create lists of numbers.

    Example:

    numbers = [1, 2, 3, 4, 5]

    doubled = [number * 2 for number in numbers]

    print(doubled)

    Output:

    [2, 4, 6, 8, 10]

    Explanation:

    Python multiplies every number by 2 and stores
    the results in a new list.

    D. List Comprehension with Strings

    List comprehensions can also work with strings.

    Example:

    names = ["Helen", "John", "Mary"]

    uppercase_names = [name.upper() for name in names]

    print(uppercase_names)

    Output:

    ['HELEN', 'JOHN', 'MARY']

    Explanation:

    - names contains three names.
    - name.upper() converts each name to uppercase.
    - The converted names are stored in a new list.

    E. List Comprehension with Conditions

    We can use an if statement inside a list comprehension
    to select items that meet a particular condition.

    Example:

    numbers = [1, 2, 3, 4, 5, 6]

    even_numbers = [number for number in numbers if number % 2 == 0]

    print(even_numbers)

    Output:

    [2, 4, 6]

    Explanation:

    - The for loop checks every number.
    - The if statement checks whether the number is even.
    - Only even numbers are added to the new list.

    F. Selecting Odd Numbers

    We can also use list comprehension to select odd numbers.

    Example:

    numbers = [1, 2, 3, 4, 5, 6]

    odd_numbers = [number for number in numbers if number % 2 != 0]

    print(odd_numbers)

    Output:

    [1, 3, 5]

    Explanation:

    The condition number % 2 != 0 selects numbers
    that are not divisible by 2 without a remainder.

    G. List Comprehension with if and else

    We can use both if and else to choose between two values.

    Example:

    numbers = [1, 2, 3, 4, 5]

    results = [
        "Even" if number % 2 == 0 else "Odd"
        for number in numbers
    ]

    print(results)

    Output:

    ['Odd', 'Even', 'Odd', 'Even', 'Odd']

    Explanation:

    - If a number is divisible by 2, Python returns "Even".
    - Otherwise, Python returns "Odd".
    - The results are stored in a new list.

    H. Using List Comprehension with range()

    We can use range() to generate values for a new list.

    Example:

    numbers = [number for number in range(1, 6)]

    print(numbers)

    Output:

    [1, 2, 3, 4, 5]

    Explanation:

    range(1, 6) generates numbers starting from 1 up to 5.

    The list comprehension places those numbers inside a list.

    I. List Comprehension with Mathematical Operations

    We can perform mathematical calculations while creating lists.

    Example:

    numbers = [1, 2, 3, 4, 5]

    cubes = [number ** 3 for number in numbers]

    print(cubes)

    Output:

    [1, 8, 27, 64, 125]

    Explanation:

    The ** operator raises a number to a power.

    number ** 3 means the number multiplied by itself three times.

    J. When Should We Use List Comprehension?

    List comprehensions are useful when:

    - Creating a new list from an existing list.
    - Performing simple calculations on list items.
    - Filtering items using conditions.
    - Converting values from one form to another.
    - Writing shorter and readable code.

    However, when the logic becomes too complicated,
    a normal for loop may be easier to understand.

    4. PRACTICAL EXAMPLES

    Example 1: Creating a List of Squares

    numbers = [2, 4, 6, 8]

    squares = [number ** 2 for number in numbers]

    print("Squares:", squares)

    Output:

    Squares: [4, 16, 36, 64]


    Example 2: Selecting Students Who Passed

    scores = [35, 70, 85, 40, 90]

    passed = [score for score in scores if score >= 50]

    print("Passed scores:", passed)

    Output:

    Passed scores: [70, 85, 90]


    Example 3: Extracting Long Names

    names = ["Helen", "John", "Christopher", "Mary"]

    long_names = [name for name in names if len(name) > 4]

    print(long_names)

    Output:

    ['Helen', 'Christopher']


    Example 4: Converting Temperatures

    celsius = [0, 10, 20, 30]

    fahrenheit = [
        (temperature * 9/5) + 32
        for temperature in celsius
    ]

    print(fahrenheit)

    Output:

    [32.0, 50.0, 68.0, 86.0]


    5. SUMMARY

    In this lesson, we learned that:

    - List comprehension is a shorter way of creating lists.
    - It allows us to create a new list from an existing sequence.
    - We can use expressions inside list comprehensions.
    - We can use for loops inside list comprehensions.
    - We can use if conditions to filter list items.
    - We can use if and else to choose between values.
    - We can perform mathematical operations.
    - We can work with strings and numbers.
    - Normal for loops are sometimes easier for complicated tasks.

    REMEMBER:

    List comprehension allows us to create new lists using
    a shorter and more readable expression.
    """)