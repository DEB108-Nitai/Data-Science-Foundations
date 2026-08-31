'''
==============================================================================
PYTHON COMPLETE NOTES: TUPLES (DATA STRUCTURE) 🚀
(Based on the Sheryians AI School Full Python Course)
==============================================================================
'''

'''
==============================================================================
1. INTRODUCTION TO TUPLES
Objective: Store multiple items in a single variable, similar to a list, 
but with one major difference: Tuples cannot be changed once created.

Syntax: Created using parentheses ()

THE 4 PROPERTIES OF TUPLES:
1. IMMUTABLE: You CANNOT change, add, or remove values after creation.
2. Duplicates Allowed: You can store the same value multiple times.
3. Ordered: Data maintains its sequence. Accessed via Indexing.
4. Heterogeneous: Can store multiple data types (int, float, str, functions).

Use Case: Tuples are used when you have data that should NEVER be modified 
accidentally (like configuration settings or fixed coordinates).
==============================================================================
'''

print("--- 1. Tuple Creation & Properties ---")

# Creating a basic tuple
my_tuple = (1, 2, 3, 4, 5)

# Heterogeneous and Duplicate-friendly tuple
mixed_tuple = (12, 12, 34.5, "Hello", True, print)

# Checking the type
print(f"Type of my_tuple: {type(my_tuple)}")


'''
==============================================================================
2. IMMUTABILITY (The Defining Feature)
Objective: Understand why Tuples are different from Lists.
CRITICAL RULE: If you try to reassign a value at a specific index in a Tuple,
Python will instantly crash with a TypeError.
==============================================================================
'''
print("\n--- 2. Immutability & Indexing ---")

t = (10, 20, 30, 40, 50)

# Indexing works exactly like Lists and Strings
print(f"First element: {t[0]}")
print(f"Last element (Negative Indexing): {t[-1]}")

# IMMUTABILITY TEST (Uncommenting the line below throws an error)
# t[0] = 100  
# TypeError: 'tuple' object does not support item assignment

print("Note: Tuples cannot be mutated. t[0] = 100 will cause an error!")


'''
==============================================================================
3. TUPLE TRAVERSING (Iterating over a Tuple)
Since Tuples are ordered, we can traverse them exactly like Lists.
==============================================================================
'''
print("\n--- 3. Traversing a Tuple ---")

demo_tuple = (100, 200, 300, 400)

# Method 1: Iterating Directly on Values (Cleaner)
print("Directly on Values:")
for val in demo_tuple:
    print(val, end=" ")

# Method 2: Using Index Values (Good if you need the exact position)
print("\n\nUsing Index:")
for i in range(len(demo_tuple)):
    print(demo_tuple[i], end=" ")
print()


'''
==============================================================================
4. TUPLE METHODS
Since Tuples are immutable, you cannot use methods like append(), remove(), 
or pop(). Therefore, Tuples only have TWO built-in methods.
==============================================================================
'''
print("\n--- 4. Tuple Methods ---")

a = (1, 5, 3, 5, 4, 5, 6)

# 1. index(value): Finds the FIRST index position of a specific value.
print(f"Index of first '3' is: {a.index(3)}")

# 2. count(value): Counts how many times a value appears in the tuple.
print(f"Count of '5' is: {a.count(5)}")


'''
==============================================================================
5. TUPLE UNPACKING
Objective: Extract values from a tuple and assign them to separate variables 
in a single line of code.
CRITICAL RULE: The number of variables on the left MUST EXACTLY MATCH the 
number of items inside the tuple.
==============================================================================
'''
print("\n--- 5. Tuple Unpacking ---")

# We have a tuple with 4 values
packed_tuple = (10, 20, 30, 40)

# Unpacking into 4 separate variables
w, x, y, z = packed_tuple

print(f"Unpacked -> w: {w} | x: {x} | y: {y} | z: {z}")


'''
==============================================================================
6. THE SINGLE ELEMENT TUPLE RULE
CRITICAL RULE: If you want to create a tuple with only ONE item, you MUST 
include a trailing comma. Otherwise, Python gets confused and thinks you are 
just putting a normal math expression inside parentheses.
==============================================================================
'''
print("\n--- 6. The Single Element Rule ---")

# Without a comma -> Python thinks this is just the integer 1 inside math brackets
fake_tuple = (1)
print(f"fake_tuple = (1)   -> Type: {type(fake_tuple)}")

# With a comma -> Python recognizes it as a Tuple
real_tuple = (1,)
print(f"real_tuple = (1,)  -> Type: {type(real_tuple)}")