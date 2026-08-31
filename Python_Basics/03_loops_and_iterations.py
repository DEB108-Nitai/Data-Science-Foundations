'''
==============================================================================
PYTHON COMPLETE NOTES: LOOPS & ITERATIONS 🚀
(Based on the Sheryians AI School Full Python Course)
==============================================================================
'''

'''
==============================================================================
1. INTRODUCTION TO LOOPS & THE RANGE FUNCTION
Objective: Execute a block of code multiple times efficiently without rewriting it.
CRITICAL RULE: The range() function's 'stop' parameter is always EXCLUSIVE. 
If you want to iterate up to 20, you must set the stop point to 21.

Syntax: range(start, stop, steps)
- start: Inclusive starting point (Defaults to 0 if omitted)
- stop: Exclusive ending point (Mandatory)
- steps: Jump between numbers (Defaults to 1 if omitted)
==============================================================================
'''

# --- VARIETIES OF THE RANGE FUNCTION ---

# 1. Full parameters (Start at 1, stop at 20, step by 1)
print("--- 1 to 20 ---")
for i in range(1, 21, 1):
    print(i, end=" ")
print()

# 2. Single parameter (Defaults: start at 0, step by 1)
print("\n--- Default Start (0 to 20) ---")
for i in range(21):
    print(i, end=" ")
print()

# 3. Custom forward range (20 to 50)
print("\n--- 20 to 50 ---")
for i in range(20, 51, 1):
    print(i, end=" ")
print()

# 4. Reverse range (Positive to Positive: 16 to 1)
# CRITICAL RULE: To go backwards, 'steps' must be negative (-1).
print("\n--- Reverse (16 to 1) ---")
for i in range(16, 0, -1):
    print(i, end=" ")
print()

# 5. Negative to Negative range (-5 to -15)
print("\n--- Negative Reverse (-5 to -15) ---")
for i in range(-5, -16, -1):
    print(i, end=" ")
print()


'''
==============================================================================
2. FOR LOOP PRACTICE QUESTIONS (Logic Building)
Objective: Apply loops and conditionals to solve standard algorithmic problems.
==============================================================================
'''

print("\n\n--- Q1: Print a Mathematical Table ---")
# Objective: Print a table dynamically.
# Method 1: Mathematical boundary manipulation (Printing multiples directly)
n = 5 # Example input
for i in range(n, (n * 10) + 1, n):
    print(i, end=" ")

# Method 2: Standard multiplication format
print("\nFormatted:")
for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")


print("\n--- Q2: Sum up to N terms ---")
# Objective: 1 + 2 + 3 + ... + N
n_terms = 5
total_sum = 0 # Storage variable

for i in range(1, n_terms + 1):
    total_sum += i  # Compound assignment: total_sum = total_sum + i
print(f"Total Sum up to {n_terms} is: {total_sum}")


print("\n--- Q3: Factorial of a Number ---")
# Objective: N! = N * (N-1) * ... * 1
# CRITICAL RULE: The storage variable 'fact' MUST start at 1. Multiplying by 0 returns 0.
fact_num = 5
fact = 1 

for i in range(1, fact_num + 1):
    fact *= i
print(f"Factorial of {fact_num} is: {fact}")


print("\n--- Q4: Sum of Even and Odd Numbers Separately in a Range ---")
limit = 40
even_sum = 0
odd_sum = 0

for i in range(1, limit + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print(f"Even Sum: {even_sum} | Odd Sum: {odd_sum}")


print("\n--- Q5: Print all Factors of a Number ---")
# Objective: Find numbers that perfectly divide the target (remainder == 0).
target_num = 12
print(f"Factors of {target_num}:", end=" ")

for i in range(1, target_num + 1):
    if target_num % i == 0:
        print(i, end=" ")


print("\n\n--- Q6: Check if a Number is a Perfect Number ---")
# Objective: Sum of factors (EXCLUDING the number itself) equals the original number.
perf_num = 6
factor_sum = 0

for i in range(1, perf_num): # Loop excludes perf_num
    if perf_num % i == 0:
        factor_sum += i

if factor_sum == perf_num:
    print(f"{perf_num} is a Perfect Number")
else:
    print(f"{perf_num} is NOT a Perfect Number")


print("\n--- Q7: Check if a Number is Prime ---")
# Objective: Prime numbers have exactly 2 factors (1 and itself).
prime_candidate = 23
count = 0

for i in range(1, prime_candidate + 1):
    if prime_candidate % i == 0:
        count += 1

if count == 2:
    print(f"{prime_candidate} is a Prime Number")
else:
    print(f"{prime_candidate} is NOT a Prime Number")


'''
==============================================================================
3. FOR LOOPS WITH STRINGS
Objective: Iterate over characters in a string.
==============================================================================
'''
my_string = "Sheryians"

# Method 1: Using Index Values
print("\n--- Traversal via Index ---")
for i in range(len(my_string)):
    print(my_string[i], end="-")

# Method 2: Direct Iteration
print("\n--- Direct Traversal ---")
for char in my_string:
    print(char, end="-")


print("\n\n--- Q8: Reverse a String (Without Inbuilt Functions) ---")
# CRITICAL RULE: Start at len-1 (last index), stop at -1 (to include 0), step -1.
rev_str = ""
for i in range(len(my_string) - 1, -1, -1):
    rev_str += my_string[i]

print(f"Original: {my_string} | Reversed: {rev_str}")


print("\n--- Q9: Check if String is Palindrome ---")
check_word = "naman"
rev_word = ""

for i in range(len(check_word) - 1, -1, -1):
    rev_word += check_word[i]

if check_word == rev_word:
    print(f"'{check_word}' is a Palindrome")
else:
    print(f"'{check_word}' is NOT a Palindrome")


print("\n--- Q10: Count Letters, Digits, and Special Symbols ---")
mixed_str = "Sheryians123!@#"
chars, digits, specials = 0, 0, 0

for i in mixed_str:
    if i.isdigit():  # Returns True if character is a number
        digits += 1
    elif i.isalpha(): # Returns True if character is an alphabet letter
        chars += 1
    else:
        specials += 1

print(f"Alphabets: {chars} | Digits: {digits} | Special Chars: {specials}")


'''
==============================================================================
4. LOOP CONTROL STATEMENTS (Break, Continue, Else)
Objective: Manipulate loop execution dynamically.
==============================================================================
'''

print("\n--- Loop Control Examples ---")
for i in range(1, 21):
    if i == 15:
        # 'continue' skips the rest of the current iteration
        continue 
    # (Print omitted to keep output clean, but 15 would be skipped)

for i in range(1, 21):
    if i == 15:
        # 'break' terminates the loop entirely
        print("Break hit at 15!")
        break
else:
    # CRITICAL RULE: 'else' paired with a loop ONLY executes if the loop 
    # completes naturally without ever hitting a 'break' statement.
    print("This will not print because the loop broke.")


'''
==============================================================================
5. WHILE LOOPS
Objective: Execute code as long as a dynamic condition is True.
CRITICAL RULE: The variable controlling the condition MUST be updated inside 
the loop block, otherwise an infinite loop occurs.
==============================================================================
'''

print("\n--- Basic While Loop ---")
a = 1
while a <= 5:
    print(a, end=" ")
    a += 1 # Update variable


print("\n\n--- Q11: Separate Each Digit of a Number ---")
# Logic: % 10 extracts the last digit. // 10 removes the last digit.
extract_num = 256

while extract_num > 0:
    last_digit = extract_num % 10
    print(last_digit, end=" ")
    extract_num = extract_num // 10


print("\n\n--- Q12: Reverse a Number using While Loop ---")
num_to_rev = 576
reversed_num = 0

while num_to_rev > 0:
    last_digit = num_to_rev % 10
    # Push the existing reverse number left by * 10, then append the new digit
    reversed_num = (reversed_num * 10) + last_digit
    num_to_rev = num_to_rev // 10

print(f"Reversed Integer: {reversed_num}")


print("\n--- Q13: Check if Number is Palindromic ---")
# CRITICAL RULE: Create a copy of the original number! 
# The while loop will destroy the variable down to 0, making comparison impossible.
orig_num = 121
copy_num = orig_num
rev_build = 0

while copy_num > 0:
    last_digit = copy_num % 10
    rev_build = (rev_build * 10) + last_digit
    copy_num = copy_num // 10

if orig_num == rev_build:
    print(f"{orig_num} is a Palindromic Number")
else:
    print(f"{orig_num} is NOT a Palindromic Number")


'''
==============================================================================
6. RANDOM NUMBER GUESSING GAME (Mini Project)
Objective: Demonstrate 'while True', 'break', and library imports.
==============================================================================
'''
print("\n--- Q14: Random Number Guessing Game ---")
import random

# Generate a random integer between 1 and 10
num = random.randint(1, 10)
tries = 0

# (Uncomment below to play the interactive game in your terminal!)
'''
while True: # Infinite loop setup
    guess = int(input("Please guess your number (1-10): "))
    tries += 1
    
    if guess == num:
        print(f"You are right! You guessed the number in {tries} tries.")
        break  # Loop termination
        
    elif guess < num:
        print("Go a little higher.")
        
    elif guess > num:
        print("Go a little lower.")
'''