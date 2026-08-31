'''
==============================================================================
PYTHON COMPLETE NOTES: DICTIONARIES (DATA STRUCTURE) 🚀
(Based on the Sheryians AI School Full Python Course)
==============================================================================
'''

'''
==============================================================================
1. INTRODUCTION TO DICTIONARIES (Hash Maps)
Objective: Store data in Key-Value pairs, allowing fast retrieval of values 
using a unique key instead of a numerical index.

Syntax: Created using curly braces {}.
CRITICAL RULE: An empty {} creates a Dictionary, NOT a Set!

THE 4 PROPERTIES OF DICTIONARIES:
1. Mutable: You can add, change, or remove Key-Value pairs after creation.
   (Note: Values can be changed, but Keys themselves cannot be changed directly. 
   You must delete the old key and create a new one).
2. Duplicates: KEYS must be 100% unique. VALUES can be duplicated.
3. Ordered: Follows "Insertion Order" (maintains the order you added them).
4. Heterogeneous: Keys and Values can be of almost any data type 
   (e.g., a string key holding a list value).
==============================================================================
'''

print("--- 1. Dictionary Creation & Properties ---")

# Creating an empty dictionary
empty_dict = {}
print(f"Type of empty {{}}: {type(empty_dict)}")

# Creating a populated dictionary (Key: Value)
d = {
    10: 100, 
    20: 200, 
    30: 300, 
    40: 400
}

# Values can be heterogeneous (strings, lists, etc.)
user_profile = {
    "name": "John",
    "age": 25,
    "skills": ["Python", "Machine Learning"]
}


'''
==============================================================================
2. ACCESSING & C.R.U.D OPERATIONS
Since dictionaries do NOT have numerical indexes like lists (0, 1, 2), 
the KEYS act as your indexes.
==============================================================================
'''
print("\n--- 2. CRUD Operations (Create, Read, Update, Delete) ---")

# A. READ: Accessing a value using its Key
print(f"Value at key 10: {d[10]}") # Output: 100
# print(d[50]) -> THROWS ERROR because key 50 does not exist yet.

# B. CREATE: Adding a new Key-Value pair
d[50] = 500  
print(f"After Create (50: 500): {d}")

# C. UPDATE: Overwriting an existing Key's value
d[10] = 1000 
print(f"After Update (10: 1000): {d}")

# D. DELETE: Removing a Key-Value pair completely
del d[30]
print(f"After Delete (Key 30): {d}")


'''
==============================================================================
3. DICTIONARY TRAVERSING (Iterating over a Dict)
Objective: Loop through the dictionary to access its contents.
CRITICAL RULE: When you run a standard 'for' loop on a dictionary, 
it iterates over the KEYS by default, not the values.
==============================================================================
'''
print("\n--- 3. Traversing a Dictionary ---")

print("Iterating over Keys and extracting Values:")
# 'i' captures the Keys (10, 20, 40, 50)
for i in d:
    # We use d[i] to dynamically grab the corresponding Value
    print(f"Key: {i} -> Value: {d[i]}")

print("\nIterating directly over Values:")
for val in d.values():
    print(val, end=" | ")
print()


'''
==============================================================================
4. MEMORY MANAGEMENT (Deep Link vs Shallow Copy)
Objective: Understand how Python handles copying data structures.
If you simply write `b = d`, Python does NOT create a new dictionary. 
It links 'b' to the exact same RAM location as 'd'. 
Any changes made to 'b' will also permanently alter 'd'.
==============================================================================
'''
print("\n--- 4. Memory Copying ---")

# DANGEROUS WAY (Reference / Deep Link)
b = d  
b[10] = 9999 
# Changing 'b' secretly changes 'd' too!
print(f"Original Dict after changing 'b': {d}")

# SAFE WAY (Shallow Copy)
# .copy() creates a brand new dictionary in a different RAM location.
safe_copy = d.copy()
safe_copy[10] = 100
print(f"Safe Copy modified: {safe_copy}")
print(f"Original remains untouched: {d}")


'''
==============================================================================
5. DICTIONARY METHODS
Built-in tools to manipulate dictionaries safely and efficiently.
==============================================================================
'''
print("\n--- 5. Dictionary Methods ---")

# 1. get(key): Safely fetches a value. 
# CRITICAL RULE: If the key doesn't exist, it returns 'None' instead of crashing.
print(f"Safe Get (Key 20): {d.get(20)}")
print(f"Safe Get (Key 999): {d.get(999)}") # No crash, just returns None

# 2. items(): Returns all Key-Value pairs as Tuples. Great for looping!
print(f"\nd.items(): {d.items()}")
for key, value in d.items():
    print(f"Item Loop -> {key}: {value}")

# 3. keys() & values(): Extracts only keys or only values.
print(f"\nKeys: {d.keys()}")
print(f"Values: {d.values()}")

# 4. update({key: value}): Bulk adds or overwrites multiple pairs at once.
d.update({60: 600, 70: 700})
print(f"\nAfter update(): {d}")

# 5. pop(key): Removes a specific key and RETURNS its value.
popped_val = d.pop(70)
print(f"Popped Key 70 (Value was {popped_val}). Dict: {d}")

# 6. clear(): Empties the entire dictionary.
# d.clear() 


'''
==============================================================================
6. DICTIONARY PRACTICE QUESTIONS (Logic Building)
The instructor solved these to demonstrate real-world hash map algorithms.
==============================================================================
'''

print("\n--- Q1: Merge Two Python Dictionaries ---")
d1 = {10: 100, 20: 200, 30: 300}
d2 = {40: 400, 50: 500, 60: 600}

# Logic: Loop through d2, and inject every Key-Value pair into d1.
for i in d2:
    d1[i] = d2[i] # If key exists, updates it. If not, creates it.
    
print(f"Merged Dictionary: {d1}")


print("\n--- Q2: Sum All Values in a Dictionary ---")
# Objective: Calculate total sum of 100 + 200 + 300...
dict_sum = 0

for i in d1:
    dict_sum += d1[i]  # Extract value using d1[i] and add to total

print(f"Total Sum of all values: {dict_sum}")


print("\n--- Q3: Count the Frequency of Each Element in a List ---")
# Objective: Convert a flat list into a dictionary tracking occurrences.
# List -> [1, 1, 2, 3, 3] Output -> {1: 2, 2: 1, 3: 2}

elements = [1, 1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 7, 8]
freq_dict = {}

for item in elements:
    # If the item is already registered as a Key in our dictionary
    if item in freq_dict.keys():
        freq_dict[item] += 1  # Increment its counter
    else:
        freq_dict[item] = 1   # Register it for the first time with a count of 1

print(f"Element Frequencies: {freq_dict}")


print("\n--- Q4: Combine Two Dictionaries & Add Values for Common Keys ---")
# Objective: If a key exists in BOTH dictionaries, ADD their values together.
# If it only exists in the second one, just insert it normally.

dict_A = {10: 100, 20: 200, 40: 300}
dict_B = {40: 400, 50: 500, 60: 600}

for i in dict_B:
    if i in dict_A.keys():
        # Common Key found (e.g., 40). Add B's value to A's value.
        dict_A[i] += dict_B[i]  # 300 + 400 = 700
    else:
        # New Key. Just insert it into dict_A.
        dict_A[i] = dict_B[i]

print(f"Combined Adding Commons: {dict_A}")