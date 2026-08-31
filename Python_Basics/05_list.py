'''
==============================================================================
PYTHON COMPLETE NOTES: LISTS (DATA STRUCTURE) 🚀
(Based on the Sheryians AI School Full Python Course)
==============================================================================
'''

'''
==============================================================================
1. INTRODUCTION TO LISTS
Objective: Store multiple values in a single, organized variable.
Lists are created using square brackets [].

THE 4 SUPERPOWERS OF LISTS:
1. Mutable: You can change, add, or remove values AFTER creation.
2. Duplicates Allowed: You can store the same value multiple times (e.g., [12, 12]).
3. Ordered: Data maintains the sequence of insertion. Every item gets an index 
   (a designated memory location slot).
4. Heterogeneous: A single list can store multiple data types at once 
   (e.g., integers, floats, booleans, and even functions!).
==============================================================================
'''

print("--- 1. List Creation & Properties ---")

# Heterogeneous and Duplicate-friendly list
my_list = [12, 13, 14, 15, 16, 34.5, True, print, 12, 12]

# Checking the type
print(f"Type of my_list: {type(my_list)}")


'''
==============================================================================
2. INDEXING, SLICING & MUTABILITY
Lists share the exact same indexing and slicing rules as Strings.
The difference? Strings are immutable, but Lists are MUTABLE.
==============================================================================
'''
print("\n--- 2. Indexing & Mutability ---")

l = [12, 13, 14, 15, 16]

# Indexing (0-based)
print(f"First element: {l[0]}")
print(f"Last element (Negative Indexing): {l[-1]}")

# Slicing [start : stop : step] (stop is exclusive)
print(f"Sliced List (Index 0 to 4): {l[0:5]}")

# Mutability: Changing an existing value
# In strings, word[0] = 'H' throws an error. In lists, it works perfectly!
l[0] = 100 
print(f"Mutated List (12 changed to 100): {l}")


'''
==============================================================================
3. LIST TRAVERSING (Iterating over a List)
There are two primary ways to loop through a list.
==============================================================================
'''
print("\n--- 3. Traversing a List ---")

demo_list = [10, 20, 30, 40]

# Method 1: Using Index Values (Better if you need the exact position)
print("Using Index:")
for i in range(len(demo_list)):
    print(demo_list[i], end=" ")

# Method 2: Iterating Directly on Values (Cleaner, but no index access)
print("\n\nDirectly on Values:")
for val in demo_list:
    print(val, end=" ")
print()


'''
==============================================================================
4. ALL LIST METHODS
Objective: Use Python's built-in functions to manipulate list data.
CRITICAL RULE: Methods like append(), insert(), and remove() modify the 
list IN-PLACE. They do not return a new list; they alter the original.
==============================================================================
'''
print("\n--- 4. List Methods ---")

a = [1, 3, 4, 5]

# 1. append(object): Adds an element to the VERY END of the list.
a.append(6)
a.append(7)
print(f"After append(6, 7): {a}")

# 2. insert(index, object): Inserts an element at a SPECIFIC index.
a.insert(1, 2) # Inserts '2' at index '1'. Everything else shifts right.
print(f"After insert(1, 2): {a}")

# 3. extend(iterable): Adds multiple elements to the end at once.
a.extend([8, 9, 10])
print(f"After extend([8, 9, 10]): {a}")

# 4. remove(value): Removes the FIRST occurrence of a specific value.
a.insert(2, 2) # Injecting a duplicate '2' to demonstrate
a.remove(2)    # Only the first '2' will be removed!
print(f"After remove(2): {a}")

# 5. pop(index): Removes and returns the element at the index (Default is last element).
popped_element = a.pop() # Removes 10
print(f"After pop(): {a} | Popped Element: {popped_element}")

# 6. index(value): Finds the first index position of a value.
print(f"Index of 5 is: {a.index(5)}")

# 7. count(value): Counts how many times a value appears in the list.
print(f"Count of 4: {a.count(4)}")

# 8. reverse(): Reverses the list IN-PLACE.
a.reverse()
print(f"After reverse(): {a}")

# 9. sort(): Sorts the list in ascending order.
a.sort()
print(f"After sort(): {a}")

# 10. copy(): Returns a SHALLOW COPY of the list.
b = a.copy() 

# 11. clear(): Removes ALL items, leaving an empty list [].
a.clear()
print(f"After clear(): {a}")


'''
==============================================================================
5. LIST PRACTICE QUESTIONS (Logic Building)
The core logic building exercises demonstrated by the instructor.
==============================================================================
'''

print("\n--- Q1: Print Positive and Negative Elements Separately ---")
nums = [45, 67, 12, -68, -69, 34]

print("Positive elements are:", end=" ")
for i in nums:
    if i >= 0:
        print(i, end=" ")

print("\nNegative elements are:", end=" ")
for i in nums:
    if i < 0:
        print(i, end=" ")


print("\n\n--- Q2: Mean (Average) of List Elements ---")
# Logic: Sum all elements, then divide by the total length of the list.
scores = [12, 45, 67, 89, 23, 25, 69]
total_sum = 0

for i in scores:
    total_sum += i  # Accumulate the sum

mean = total_sum / len(scores)
print(f"Mean of List: {mean}")


print("\n--- Q3: Find the Greatest Element and its Index ---")
# Logic: Assume the first item is the largest. Compare it to the rest. 
# If a bigger item is found, it becomes the new largest.
vals = [12, 36, 14, 19, 128, 6, 13]

largest = vals[0]
largest_idx = 0

for i in range(len(vals)):
    if vals[i] > largest:
        largest = vals[i]
        largest_idx = i

print(f"Largest Number is {largest} at index {largest_idx}")


print("\n--- Q4: Find the Second Largest Number ---")
# Logic: Keep track of largest and second_largest. If a new largest is found, 
# the old largest gets demoted to second_largest.
L4 = [12, 16, 13, 19, 17]

largest = L4[0]
sec_largest = L4[0]

for i in L4:
    if i > largest:
        sec_largest = largest  # Old largest gets pushed down
        largest = i            # Update the new largest
    elif i > sec_largest and i != largest:
        sec_largest = i        # Update sec_largest if it's smaller than the new element

print(f"List: {L4}")
print(f"Largest: {largest} | Second Largest: {sec_largest}")


print("\n--- Q5: Check if List is Sorted ---")
# Logic: Compare current element with the NEXT element.
# CRITICAL RULE: We must loop up to (len(list) - 1) to avoid an "Index Out of Range" error 
# when checking L[i + 1] at the very end of the loop.
check_list = [12, 13, 14, 15, 16]

for i in range(len(check_list) - 1):
    if check_list[i] <= check_list[i + 1]:
        continue # It's in order, move to the next pair
    else:
        print("Your list is NOT sorted")
        break
else:
    # This 'else' belongs to the 'for' loop. It triggers ONLY if the loop finishes 
    # entirely without hitting the 'break' statement.
    print("Your list IS sorted")


'''
==============================================================================
6. ADVANCED: LIST COMPREHENSIONS
Objective: Create a new list dynamically using a single-line expression.
Syntax: [expression for item in iterable if condition]
==============================================================================
'''
print("\n--- ADVANCED: List Comprehensions ---")

# Normal Way to get even numbers:
# evens = []
# for i in range(1, 21):
#     if i % 2 == 0:
#         evens.append(i)

# The Comprehension Way (One-liner!):
# Read as: "Append 'i', for 'i' in range 1 to 20, IF 'i' is divisible by 2"
evens_comp = [i for i in range(1, 21) if i % 2 == 0]

print(f"Even numbers (List Comprehension): {evens_comp}")