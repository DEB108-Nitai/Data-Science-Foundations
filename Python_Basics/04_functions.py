'''
==============================================================================
PYTHON COMPLETE NOTES: FUNCTIONS 🚀
(Based on the Sheryians AI School Full Python Course)
==============================================================================
'''

'''
==============================================================================
1. INTRODUCTION TO FUNCTIONS
Objective: Transition from an "Imperative Approach" (writing code line-by-line 
every time) to a "Functional Approach" (reusable blocks of code).

CRITICAL RULE: A function is a block of code that ONLY runs when it is called.

REAL-LIFE ANALOGY (From the Video):
Imagine a friend named Python. You assign him a task named "Water". 
If you say "Pani" (water in Hindi), nothing happens. But the moment you call 
the exact function name "Water", he hands you a glass of water. You can call 
"Water" as many times as you want!
==============================================================================
'''

print("--- 1. Creating and Calling a Function ---")

# Step 1: Define the function using the 'def' keyword
def hello():
    # Indentation is mandatory here
    print("This is a hello function, so I am doing hello")

# Step 2: Call the function (Without calling, it does nothing!)
hello()


'''
==============================================================================
2. PARAMETERS AND ARGUMENTS
Objective: Make functions dynamic by passing data into them.
CRITICAL RULE: 
- PARAMETERS: The variables you define inside the function parentheses (a, b). 
  (They "accept" the data).
- ARGUMENTS: The actual values you pass into the function when calling it.
  (They "provide" the data).
==============================================================================
'''

print("\n--- 2. Parameters & Arguments ---")

def addition(a, b): # 'a' and 'b' are PARAMETERS
    print(f"The sum of your numbers is {a + b}")

# Calling the function and passing ARGUMENTS (12 and 45)
addition(12, 45) 
addition(56, 89) # Reusing the exact same function with different data


'''
==============================================================================
3. TYPES OF ARGUMENTS
There are 3 main ways to pass arguments to parameters in Python.
==============================================================================
'''

print("\n--- 3. Types of Arguments ---")

# A. POSITIONAL ARGUMENTS
# The first argument goes to the first parameter, the second to the second, etc.
def user_details(name, age):
    print(f"Your name is {name} and your age is {age}")

user_details("Akarsh", 22) # Mapped by their exact position


# B. KEYWORD ARGUMENTS
# You explicitly mention the parameter name. Order no longer matters!
user_details(age=22, name="Akarsh") 


# C. DEFAULT ARGUMENTS
# You provide a default value in the function definition. 
# If the caller forgets to pass that argument, the default kicks in.
def default_addition(a, b=45):
    print(f"The sum is: {a + b}")

default_addition(12)      # Only passed 'a'. 'b' defaults to 45. (12 + 45)
default_addition(12, 34)  # Passed both. 'b' is reassigned to 34. (12 + 34)


'''
==============================================================================
4. THE RETURN STATEMENT
Objective: Instead of just printing a result inside the function, you 
"return" the value back to wherever the function was called from.
CRITICAL RULE: 'return' sends data back and immediately EXITS the function.
==============================================================================
'''

print("\n--- 4. Print vs Return ---")

def greeting_print():
    print("Hello, how are you?") # Just prints it to the terminal

def greeting_return():
    return "Hello, how are you?" # Hands the string back to the caller

# Calling the print version
greeting_print() 

# Calling the return version
# Notice we MUST wrap it in print() to see it, otherwise it just returns the 
# data invisibly in the background.
print(greeting_return()) 


'''
==============================================================================
5. FUNCTION PRACTICE: PALINDROME CHECKER
Objective: Wrap previous string reversal logic inside a reusable function.
==============================================================================
'''

print("\n--- 5. Practice: Palindrome Checker Function ---")

def check_palindrome(st):
    rev = ""
    # Reverse the string manually
    for i in range(len(st) - 1, -1, -1):
        rev += st[i]
        
    if rev == st:
        print(f"'{st}' is a Palindrome")
    else:
        print(f"'{st}' is NOT a Palindrome")

# Testing the function with multiple strings
check_palindrome("naman")
check_palindrome("cursor")

'''
==============================================================================
END OF BASIC FUNCTIONS
Next in the instructor's timeline -> Data Structures (Lists, Tuples, Sets, Dicts)
==============================================================================
'''