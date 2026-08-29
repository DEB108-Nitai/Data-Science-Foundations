'''
==============================================================================
PYTHON COMPLETE NOTES: CONDITIONAL STATEMENTS 🚀
(Based on the Sheryians AI School Full Python Course)
==============================================================================
'''

'''
==============================================================================
1. THE CONCEPT OF CONDITIONAL STATEMENTS
Conditional statements allow your program to make decisions. 
Based on a condition (which evaluates to True or False), the program will 
execute different blocks of code. This controls the "flow" of the program.

CRITICAL RULE: INDENTATION
Python does not use curly braces {} to define code blocks. Instead, it uses 
indentation (usually 4 or 5 spaces). If you don't indent properly after an 
if/elif/else statement, Python will throw an 'IndentationError'.
==============================================================================
'''

# --- The Ice Cream Analogy (Basic if, elif, else) ---
# Scenario: Mom gives you money. 
# If ₹10 -> Choco bar. If ₹20 -> Mango Dolly. If ₹30 or more -> Cone.

money = 20  # You can change this to 10, 20, 30 to test

if money == 10:
    # This block runs ONLY if the condition 'money == 10' is True
    print("I will have a Choco bar ice cream.")

elif money == 20:
    # 'elif' checks a new condition if the previous 'if' was False
    print("I will have a Mango Dolly.")

elif money >= 30:
    # You can have multiple elif statements in a sequence (a ladder)
    print("I will have a Cone.")

else:
    # 'else' has no condition. It acts as a fallback if EVERYTHING above is False.
    print("I don't have the exact amount for a specific ice cream.")


'''
==============================================================================
2. PRACTICE QUESTIONS SOLVED IN THE VIDEO
These questions build logic by combining inputs, type conversion, 
comparison operators, and if-else ladders.

(Note: The input() prompts are provided below. If you run this script, 
you can change the hardcoded variables to test the logic directly.)
==============================================================================
'''

print("\n--- Q1: Greatest Between Two Numbers ---")
# Objective: Accept two numbers and print the greatest between them.

num1 = 34  # In video: int(input("Please tell your first number: "))
num2 = 56  # In video: int(input("Please tell your second number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    # Edge case: What if both numbers are exactly the same?
    print("Both numbers are same")


print("\n--- Q2: Gender Greeting ---")
# Objective: Accept gender as a character ('m' or 'f') and print a greeting.
# Handles both uppercase and lowercase inputs using Logical 'or'.

gender = 'm'  # In video: input("Please tell your gender (m/f): ")

if gender == 'm' or gender == 'M':
    print("Good morning Sir")
elif gender == 'f' or gender == 'F':
    print("Good morning Mam")
else:
    # Edge case: What if the user types 'q' or 'e'?
    print("Unidentified gender")


print("\n--- Q3: Even or Odd Number ---")
# Objective: Accept an integer and check if it is Even or Odd.

num_to_check = 345  # In video: int(input("Please tell your number: "))

# Logic: An even number is perfectly divisible by 2 (remainder is 0).
if num_to_check % 2 == 0:
    print("Even number")
else:
    print("Odd number")


print("\n--- Q4: Valid Voter Check ---")
# Objective: Accept name and age, check if the user is a valid voter (18+).

voter_name = "Shery" # In video: input("Please tell your name: ")
voter_age = 17       # In video: int(input("Now tell your age: "))

if voter_age >= 18:
    print(f"Hello {voter_name}, you are a valid voter.")
else:
    print(f"Hello {voter_name}, you are NOT a valid voter.")


print("\n--- Q5: Leap Year Logic ---")
# Objective: Accept a year and check if it's a leap year.
# Critical Logic: Century years (ending in 00) must be checked with 400. 
# Normal years are checked with 4.

year = 2004  # In video: int(input("Please tell your year: "))

if year % 100 == 0 and year % 400 == 0:
    # It is a century year AND divisible by 400
    print("It's a leap year")
elif year % 100 != 0 and year % 4 == 0:
    # It is NOT a century year, but divisible by 4
    print("It's a leap year")
else:
    # Fails both leap year conditions
    print("It's a normal year")


print("\n--- Q6: The If-Elif Ladder (Temperature Check) ---")
# Objective: Check temperature in Celsius and print the weather condition using ranges.

temp = 34  # In video: int(input("Please tell the temperature: "))

if temp < 0:
    print("Freezing Cold")
elif temp >= 0 and temp < 10:
    # Combining two conditions using Logical 'and' to define a strict range
    print("Very Cold")
elif temp >= 10 and temp < 20:
    print("Cold")
elif temp >= 20 and temp < 30:
    print("Pleasant")
elif temp >= 30 and temp < 40:
    print("Hot")
else:
    # If it is 40 or above, the 'else' fallback automatically catches it
    print("Very Hot")

'''
==============================================================================
END OF CONDITIONAL STATEMENTS
Next Steps -> Loops (for, while, range function)
==============================================================================
'''