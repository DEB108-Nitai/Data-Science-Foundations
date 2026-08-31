# ==============================================================================
# PYTHON COMPLETE NOTES: BASICS TO OPERATORS 🚀
# (Based on the Sheryians AI School Full Python Course)
# ==============================================================================

'''
1. COMMENTS IN PYTHON
Comments are parts of the code that the Python interpreter completely ignores.
If you write random text like 'Hello I am Akarsh' in your editor, Python 
throws an error. Comments fix this.
'''

# A. Single-Line Comments: Use a hashtag (#). The interpreter skips this line.
print("Hello World")  # This prints a message to the console

# B. Multi-Line Comments (Docstrings): 
# Python doesn't have an official multi-line comment. Instead, we use "Docstrings" 
# by wrapping text in three quotes (''' or """). If it's not assigned to a variable, 
# Python ignores it, making it act like a multi-line comment.
'''
Hello, this is multi-line.
You can write paragraphs here without any errors.
'''


# ==============================================================================
# 2. VARIABLES
# ==============================================================================
'''
The Storage Analogy: Think of variables like a storage container or a gym bottle. 
In a bottle, you can store water, milk, or wine. A variable is just a storage space 
where you can keep data.

Rules for Naming Variables:
1. No numbers at the start: `1sher` is an error, but `sher1` is fine.
2. No spaces allowed: `sheryians school` throws an error.
3. No special characters: Don't use @, !, %, $, etc. (Underscore `_` is allowed).

Naming Conventions:
- PascalCase: SheryiansSchool
- camelCase: sheryiansSchool
- snake_case: sheryians_school (Most recommended in Python!)
'''

sher = "Harsh Bhaiya" # Creating a variable and storing a string
a = 12                # Storing a number


# ==============================================================================
# 3. DATA TYPES
# ==============================================================================
'''
Variables store data, but what type of data?
1. Integer (int): Natural numbers (1, 2, 3), whole numbers (0), negative numbers.
2. Float (float): Any number with a decimal (1.5). Also, any number in fraction 
   form (p/q). Even 12/3 is stored as 4.0.
3. Complex (complex): Used in math for imaginary values using 'j' (e.g., 34 + 5j).
4. Strings (str): Text data. Anything inside quotes. (No 'char' type in Python).
5. Boolean (bool): Stores only True or False (T and F must be capital).
'''

num_int = 12              
num_float = 12 / 3          
num_complex = 34 + 5j         
my_string = "Hello 123 !@" 
is_valid = True          

# Checking types using the type() function
print(type(num_float)) # Output: <class 'float'>


# ==============================================================================
# 4. STRINGS & TYPE CONVERSION DEEP DIVE
# ==============================================================================
'''
Strings & Unicodes:
Every character has a specific Unicode (ASCII value).
- ord() gives the Unicode number. ord('A') is 65.
- chr() converts the number back to the character. chr(65) gives 'A'.

String Indexing (0-based):
Positive: S=0, H=1, E=2, R=3
Negative: R=-1, E=-2, H=-3, S=-4 (Starts from the end)
'''
word = "SHER CODER"

# String Slicing [start : stop : steps] -> Note: 'stop' is exclusive!
print(word[0:4:1]) # Outputs "SHER" (Index 0 to 3)
print(word[5::])   # Outputs "CODER" (Starts at 5, goes to the end)
print(word[::-1])  # Quick way to reverse a string -> REDOC REHS

'''
Type Conversion:
- Implicit: Python does it automatically (e.g., 12 / 3 -> 4.0).
- Explicit: We force it using int(), float(), str(), bool().

Boolean Truthy & Falsy Values:
When converting values to bool(), almost everything becomes True EXCEPT 7 values:
False, 0, 0.0, "" (Empty String), [] (Empty List), () (Empty Tuple), {} (Empty Dict)
'''
# Explicit conversion
num_str = "12"
converted_num = int(num_str) 

print(bool(0))     # False (Falsy value)
print(bool("Hi"))  # True (Truthy value)


# ==============================================================================
# 5. INPUT AND OUTPUT
# ==============================================================================
'''
Output: print()
Formatted Strings (f-strings): To avoid writing multiple strings and commas, 
we use an 'f' before the string and inject variables inside curly brackets {}.
'''
name = "Akarsh"
age = 23
print(f"My name is {name} and my age is {age}")

'''
Input: input()
Crucial Rule: By default, input() ALWAYS captures data as a String. 
If you want to do math with it, you MUST explicitly convert it using int() or float().
'''
# Uncomment the lines below to test input functionality in your terminal
# user_name = input("What is your name? ")
# user_age = int(input("What is your age? ")) 
# print(f"Hello {user_name}, next year you will be {user_age + 1} years old.")


# ==============================================================================
# 6. OPERATORS
# ==============================================================================

# A. Arithmetic Operators ------------------------------------------------------
a = 20
b = 5

print(a + b)  # Addition: 25
print(a - b)  # Subtraction: 15
print(a * b)  # Multiplication: 100
print(a / b)  # Normal Division: 4.0 (Always returns a Float)
print(a // b) # Floor Division: 4 (Removes decimal, returns Integer)
print(a % 3)  # Modulo: 2 (Returns the Remainder of 20/3)
print(b ** 2) # Exponential (Power): 25 (5 to the power of 2)

# B. Assignment / Compound Operators -------------------------------------------
# Used to update a variable based on its previous value.
x = 10     
x += 5     # Equivalent to x = x + 5 (x becomes 15)
x *= 2     # Equivalent to x = x * 2 (x becomes 30)

# C. Comparison Operators ------------------------------------------------------
# Compares values and returns a Boolean.
num1 = 12
num2 = 15

print(num1 == num2) # Equal to: False
print(num1 != num2) # Not equal to: True
print(num1 > num2)  # Greater than: False
print(num1 < num2)  # Less than: True
print(num1 >= 12)   # Greater than or equal to: True

# Comparing Strings: Done based on ASCII values letter by letter.
print("A" > "B") # False (ASCII 65 is not greater than 66)

# D. Logical Operators ---------------------------------------------------------
# Combines conditional statements.
# 1. and: ALL conditions must be True.
print((10 > 5) and (5 > 2)) # True

# 2. or: At least ONE condition must be True.
print((12 < 10) or (45 == 45)) # True

# 3. not: Reverses the boolean state.
print(not (10 == 10)) # False (10 == 10 is True, 'not' reverses it)