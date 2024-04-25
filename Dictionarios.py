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
