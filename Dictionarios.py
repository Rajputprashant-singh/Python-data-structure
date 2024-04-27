# Theoretical Overview:

# What is a Dictionary?
# - A dictionary is a built-in data structure in Python used to store collections of key-value pairs.
# - It is unordered, meaning the items do not have a defined order.
# - Dictionaries are mutable, meaning you can modify their contents after creation.
# - Each key in a dictionary must be unique.

# Creating Dictionaries:
# - Dictionaries are created using curly braces {}.
# - Key-value pairs are separated by colons (:), and pairs are separated by commas.

# Accessing Dictionary Elements:
# - Dictionary elements are accessed using keys rather than indices.
# - Keys can be of any immutable type, such as strings, numbers, or tuples.

# Dictionary Operations:
# - Adding elements: Assigning a value to a new key.
# - Removing elements: Using the del keyword or the pop() method.
# - Updating elements: Assigning a new value to an existing key.
# - Dictionary methods: Include keys(), values(), items(), etc.

# Practical Examples with Exercises:

# Example 1: Creating and Accessing Dictionaries
# Create a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Access value using key
print("Name:", my_dict['name'])

# Exercise: Access the value associated with the key 'age'.

# Example 2: Adding and Updating Elements
# Add a new key-value pair
my_dict['gender'] = 'Male'

# Update the value of an existing key
my_dict['age'] = 35

# Print the updated dictionary
print("Updated dictionary:", my_dict)

# Exercise: Add a new key-value pair with key 'occupation' and value 'Engineer'.

# Example 3: Dictionary Methods
# Get all keys
keys = my_dict.keys()
print("Keys:", keys)

# Get all values
values = my_dict.values()
print("Values:", values)

# Get all key-value pairs (items)
items = my_dict.items()
print("Items:", items)

# Exercise: Use the items() method to print all key-value pairs of the dictionary.

# Questions:

# 1. What is the difference between a dictionary and a list in Python?
# 2. Can the keys in a dictionary be mutable? Why or why not?
# 3. How can you remove a key-value pair from a dictionary?
# 4. What are some common dictionary methods and their uses?
# 5. Can a dictionary have duplicate keys? Why or why not?





I'd be glad to provide a comprehensive response on Python dictionaries, combining the best aspects of theory and practical questions:

**Theory: Python Dictionaries**

* **Definition:** A dictionary is a mutable unordered data structure that stores key-value pairs. Each key is unique and acts as an identifier for its associated value. Keys can be of any immutable data type (strings, numbers, tuples), while values can be of any data type (including other dictionaries or lists).
* **Syntax:**

```python
my_dict = {"key1": value1, "key2": value2, ...}
```

* **Basic Operations:**
    - **Accessing Values:** Use the key enclosed in square brackets `[]` to retrieve the value associated with that key.
        ```python
        value = my_dict["key1"]
        ```
    - **Adding Key-Value Pairs:** Use assignment with the key within square brackets.
        ```python
        my_dict["key3"] = "new_value"
        ```
    - **Modifying Values:**  Assign a new value to an existing key.
        ```python
        my_dict["key2"] = "updated_value"
        ```
    - **Removing Key-Value Pairs:** Use `del` keyword or `pop` method (returns the value).
        ```python
        del my_dict["key1"]
        removed_value = my_dict.pop("key2")
        ```
    - **Checking Key Existence:** Use the `in` operator.
        ```python
        if "key3" in my_dict:
            print("Key exists")
        ```
    - **Iterating:** You can iterate over keys, values, or both key-value pairs.
        ```python
        for key in my_dict:  # Iterates over keys
            print(key)

        for value in my_dict.values():  # Iterates over values
            print(value)

        for key, value in my_dict.items():  # Iterates over key-value pairs
            print(key, value)
        ```

* **Built-in Methods:** Dictionaries offer various methods for common operations. Refer to Python documentation for a complete list: [https://docs.python.org/3/c-api/dict.html](https://docs.python.org/3/c-api/dict.html). Here are some common ones:
    - `get(key, default)`: Gets the value for a key, returning a default value if the key is not found.
    - `keys()`: Returns a view of all keys in the dictionary.
    - `values()`: Returns a view of all values in the dictionary.
    - `items()`: Returns a view of all key-value pairs as tuples.
    - `update(other_dict)`: Updates the dictionary with key-value pairs from another dictionary.
    - `clear()`: Removes all key-value pairs from the dictionary.

**Practical Questions:**

1. **Create a dictionary to store information about your favorite books, with keys like title, author, genre, and year published.**

```python
books = {
    "title": "The Hitchhiker's Guide to the Galaxy",
    "author": "Douglas Adams",
    "genre": "Science Fiction",
    "year_published": 1979
}
```

2. **Write a function that takes a dictionary as input and returns the sum of all the values if they are numerical.**

```python
def sum_values(data):
    total = 0
    for value in data.values():
        if isinstance(value, (int, float)):
            total += value
    return total

# Example usage
data = {"a": 10, "b": "hello", "c": 3.14}
total_sum = sum_values(data)
print(total_sum)  # Output: 13.14
```

3. **Write a program that reads student names and scores from the user and stores them in a dictionary. Then, print the name of the student with the highest score.**

```python
students = {}
while True:
    name = input("Enter student name (or 'q' to quit): ")
    if name.lower() == 'q':
        break
    score = float(input("Enter student score: "))
    students[name] = score

highest_score = max(students.values())
for name, score in students.items():
    if score == highest_score:
        print(f"Student with highest score: {name} ({highest_score})")
```

These are just a few examples. Dictionaries are versatile data structures used extensively in Python for various tasks. Practice using them to solve problems