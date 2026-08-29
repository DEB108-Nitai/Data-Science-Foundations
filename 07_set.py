'''
==============================================================================
PYTHON COMPLETE NOTES: SETS (DATA STRUCTURE) 🚀
(Based on the Sheryians AI School Full Python Course)
==============================================================================
'''

'''
==============================================================================
1. INTRODUCTION TO SETS
Objective: Store multiple unique items in a single variable.

Syntax: Created using curly braces {} 
CRITICAL RULE: An empty pair of curly braces {} creates a Dictionary, NOT a Set! 
To create an empty set, you must use the set() function.

THE 4 PROPERTIES OF SETS:
1. Mutable: You can add or remove items from the set after creation.
2. NO DUPLICATES ALLOWED: Every element must be entirely unique. 
   If you try to add a duplicate, Python simply ignores it.
3. UNORDERED: Data does not maintain the sequence of insertion. 
   There is NO INDEXING. You cannot access elements like s[0].
4. Semi-Heterogeneous: Can store multiple data types, but ONLY 'hashable' 
   (immutable) objects like integers, strings, and tuples. You CANNOT store 
   a List or Dictionary inside a Set.
==============================================================================
'''

print("--- 1. Set Creation & Properties ---")

# Creating a basic set with duplicate values
s = {1, 2, 3, 4, 5, 5, 4}

# Notice that the duplicates (4, 5) are automatically removed when printed
print(f"Set automatically removes duplicates: {s}")

# Checking the type
print(f"Type of s: {type(s)}")


'''
==============================================================================
2. THE HASHING CONCEPT (Under the Hood)
Objective: Understand WHY Sets are unordered and have no indexes.

How does a Set store values in RAM? 
Unlike a List (which stores items linearly in a numbered order like 0, 1, 2), 
a Set takes your value and runs it through a hash() function. 
This hash function generates a massive, random memory location number. 

Because the memory location is completely random (based on the hash), 
the Set doesn't know what "Index 0" or "Index 1" means. That is why 
Sets are strictly UNORDERED.
==============================================================================
'''
print("\n--- 2. Hashing Concept ---")

# Python has an in-built hash() function that sets use behind the scenes
print(f"Hash value of integer 12: {hash(12)}")
print(f"Hash value of string 'Hello': {hash('Hello')}")

# CRITICAL RULE: Unordered means NO INDEXING
# Uncommenting the line below will crash the program with a TypeError:
# print(s[0]) 
# TypeError: 'set' object is not subscriptable


'''
==============================================================================
3. SET TRAVERSING (Iterating over a Set)
Since Sets have no index, you CANNOT use the range(len()) method.
You must iterate directly over the values.
==============================================================================
'''
print("\n--- 3. Traversing a Set ---")

demo_set = {10, 20, 30, 40, "Hello"}

# Traversing directly on values (Notice the output order might look random)
for val in demo_set:
    print(val, end=" | ")
print()


'''
==============================================================================
4. SET METHODS
Objective: Use Python's built-in functions to manipulate set data.
Since there are no indexes, methods do not rely on positions.
==============================================================================
'''
print("\n--- 4. Set Methods ---")

a = {1, 3, 4}

# 1. add(value): Adds a single element to the set.
a.add(6)
print(f"After add(6): {a}")

# 2. remove(value): Removes a specific value.
# CRITICAL RULE: Throws a KeyError if the value does NOT exist!
a.remove(3)
print(f"After remove(3): {a}")

# 3. discard(value): Removes a specific value SAFELY.
# CRITICAL RULE: Does NOT throw an error if the value is missing.
a.discard(100) # 100 doesn't exist, but the code won't crash
print(f"After discard(100): {a}")

# 4. pop(): Removes and returns a RANDOM element.
# Since sets are unordered, you never know exactly which item will pop!
popped_item = a.pop()
print(f"After pop(): {a} | Popped Item: {popped_item}")

# 5. clear(): Empties the entire set, leaving set()
a.clear()
print(f"After clear(): {a}")


'''
==============================================================================
5. MATHEMATICAL SET OPERATIONS (Venn Diagram Concepts)
Objective: Compare multiple sets against each other to find commonalities 
or differences. Python has special short-hand operators for this.
==============================================================================
'''
print("\n--- 5. Set Operations ---")

# Let's imagine two circles in a Venn Diagram
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(f"Set A: {A}")
print(f"Set B: {B}\n")

# A. UNION (| pipe operator)
# Combines everything from both sets, removing duplicates.
# Long form: A.union(B)
print(f"Union (A | B): {A | B}")              

# B. INTERSECTION (& ampersand operator)
# Extracts ONLY the elements that exist in BOTH sets.
# Long form: A.intersection(B)
print(f"Intersection (A & B): {A & B}")         

# C. DIFFERENCE (- minus operator)
# Extracts elements that are strictly in the first set, excluding any common items.
# Long form: A.difference(B)
print(f"Difference (A - B): {A - B}")   

# D. SYMMETRIC DIFFERENCE (^ caret operator)
# Extracts everything EXCEPT the common elements. (The exact opposite of Intersection).
# Long form: A.symmetric_difference(B)
print(f"Symmetric Difference (A ^ B): {A ^ B}")       


'''
==============================================================================
6. COMPOUND SET OPERATIONS
Objective: Perform an operation and instantly update the original set.
Just like x += 5, we can use compound operators on sets.
==============================================================================
'''
print("\n--- 6. Compound Set Operations ---")

# Let's say we want Set B to permanently become the difference of (B - A)
B -= A  

# Set B originally had {4, 5, 6, 7, 8}. 
# A had {1, 2, 3, 4, 5}. 
# B - A removes the common elements (4, 5) from B permanently.
print(f"Set B after (B -= A): {B}")