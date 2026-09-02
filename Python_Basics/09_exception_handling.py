'''
==============================================================================
PYTHON COMPLETE NOTES: EXCEPTION HANDLING 🚀
(Based on the Sheryians AI School Full Python Course)
==============================================================================
'''

'''
==============================================================================
1. ERRORS VS. EXCEPTIONS
Objective: Understand the difference between code mistakes that break the 
program completely, and unexpected events that can be managed.

A. ERRORS (Cannot be handled):
   Mistakes in how the code is written. Python cannot run the code at all.
   - SyntaxError: Missing a bracket, quote, or colon.
   - IndentationError: Forgetting to use 5 spaces/Tab after an 'if' or 'for'.
   - TabError: Mixing spaces and tabs.

B. EXCEPTIONS (Can be handled):
   The code is written perfectly, but an unexpected event happens during 
   execution (runtime) that disrupts the normal flow.
   Example: The user enters '0' and the program tries to divide by zero 
   (ZeroDivisionError), or tries to divide a string by an integer.
==============================================================================
'''

print("--- 1. Understanding Exceptions ---")

# Let's simulate a scenario where the user provides a number for division.
# divisor = int(input("Tell your number: "))
divisor = 0  # Hardcoded to 0 to simulate the error

# If we just run: print(10 / divisor)
# The program would instantly CRASH here with a ZeroDivisionError, 
# and no code below it would ever execute.


'''
==============================================================================
2. THE 'try' AND 'except' BLOCKS
Objective: Prevent the program from crashing by "catching" the exception.

CRITICAL RULE: The 'try' block MUST be followed by at least one 'except' 
or 'finally' block. You cannot use 'try' alone.
==============================================================================
'''
print("\n--- 2. Try and Except ---")

try:
    # We wrap the "risky" code inside the try block
    result = 10 / divisor
    print(f"Result is: {result}")

except ZeroDivisionError:
    # If a ZeroDivisionError occurs in the try block, the program jumps here
    # instead of crashing.
    print("Sorry, you cannot divide by zero!")

print(">>> Program continues to run normally after the except block! <<<")


'''
==============================================================================
3. CATCHING ANY EXCEPTION DYNAMICALLY
Objective: Handle errors when you don't know exactly what might go wrong.
We can use 'Exception as err' to catch ANY error and store its description.
==============================================================================
'''
print("\n--- 3. Catching All Exceptions ---")

# Let's simulate a TypeError (Dividing a string by an int)
# risky_input = input("Tell your number: ") # User types "Hello"
risky_input = "Hello"

try:
    # Dividing an integer by a string will throw a TypeError
    ans = 10 / risky_input
    print(ans)

except Exception as err:
    # Catches the error and prints the system's exact error message
    print(f"Sorry, there is an error: {err}")


'''
==============================================================================
4. THE 'else' AND 'finally' BLOCKS
Objective: Execute specific code based on whether an exception occurred or not.

CRITICAL RULE: 
- 'else' block runs ONLY IF the 'try' block succeeds with NO EXCEPTIONS.
- 'finally' block runs NO MATTER WHAT (whether an error happened or not). 
  It acts like a boss/cleanup crew.
==============================================================================
'''
print("\n--- 4. Else and Finally ---")

# Let's simulate a successful division this time
valid_divisor = 5

try:
    print(f"Attempting division: 10 / {valid_divisor}")
    res = 10 / valid_divisor

except Exception as err:
    print(f"An error occurred: {err}")

else:
    # Runs because 10 / 5 was successful!
    print(f"Good! There is no exception. The answer is {res}")

finally:
    # Runs absolutely every time.
    print("I will run no matter what! (Executing Finally Block)")


'''
==============================================================================
5. THE 'raise' KEYWORD (Manual Exceptions)
Objective: Create and throw your own custom exceptions based on your business 
logic, even if Python doesn't think it's a technical error.
==============================================================================
'''
print("\n--- 5. Manually Raising Exceptions ---")

# Scenario: A club admits only people between the ages of 10 and 18.
# user_age = int(input("Tell your age: "))
user_age = 50  # Hardcoded to 50, which violates our rule

try:
    if user_age < 10 or user_age > 18:
        # Python doesn't care if age is 50, but OUR logic cares.
        # We manually trigger a ValueError and provide our own custom message.
        raise ValueError("Your age must be between 10 and 18 to enter.")
    
    print("Welcome to the club!")

except Exception as err:
    # The 'raise' command immediately throws the error down to this except block.
    print(f"An error occurred: {err}")

# Since we handled our own manually raised error, the program survives!
print("The club will start soon. (Program executed successfully)")