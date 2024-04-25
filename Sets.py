# Theoretical Overview:

# What is a Set?
# - A set is a built-in data structure in Python used to store unique elements.
# - It is unordered, meaning the elements do not have a defined order.
# - Sets are mutable, meaning you can modify their contents after creation.
# - Sets do not allow duplicate elements.

# Creating Sets:
# - Sets are created using curly braces {}.
# - Elements are separated by commas.

# Accessing Set Elements:
# - Since sets are unordered, elements cannot be accessed by indices.
# - However, you can check for membership using the in operator.

# Set Operations:
# - Adding elements: Use the add() method or the update() method to add multiple elements.
# - Removing elements: Use the remove() or discard() method, or the pop() method to remove and return an arbitrary element.
# - Set methods: Include union(), intersection(), difference(), symmetric_difference(), etc.

# Practical Examples with Exercises:

# Example 1: Creating and Accessing Sets
# Create a set
my_set = {1, 2, 3, 4, 5}

# Check if an element exists in the set
print("Is 3 in the set?", 3 in my_set)

# Exercise: Check if 6 is in the set.

# Example 2: Adding and Removing Elements
# Add an element to the set
my_set.add(6)

# Remove an element from the set
my_set.remove(3)

# Print the updated set
print("Updated set:", my_set)

# Exercise: Remove an arbitrary element from the set using the pop() method.

# Example 3: Set Operations
# Create two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union of sets
union_set = set1.union(set2)
print("Union set:", union_set)

# Intersection of sets
intersection_set = set1.intersection(set2)
print("Intersection set:", intersection_set)

# Exercise: Find the difference between set1 and set2 using the difference() method.

# Questions:

# 1. What is the primary characteristic of sets that distinguishes them from lists and tuples?
# 2. Can sets contain duplicate elements? Why or why not?
# 3. How can you add or remove elements from a set?
# 4. What are some common set methods and their uses?
# 5. How can you perform set operations such as union, intersection, and difference in Python?
