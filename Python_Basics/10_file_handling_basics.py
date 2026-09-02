'''
==============================================================================
PYTHON COMPLETE NOTES: FILE HANDLING (BASICS) 🚀
(Based on the Sheryians AI School Full Python Course)
==============================================================================
'''

'''
==============================================================================
1. INTRODUCTION TO FILE HANDLING
Objective: Interact with files on your computer to perform C.R.U.D operations
(Create, Read, Update, Delete) dynamically using Python.

Any name with an extension is a file (e.g., main.py, hello.txt, data.json).
Whenever we want to handle these files programmatically, we use File Handling.

THE open() FUNCTION:
Python uses the built-in open() function to access files.
Syntax: open(file_path, mode)
- file_path: The location and name of the file (e.g., "superman.txt").
- mode: The purpose for opening the file (Read, Write, Append, etc.).
==============================================================================
'''

print("--- 1. File Handling Modes ---")
'''
CRITICAL RULE: There are 4 primary modes in File Handling:
1. 'r' (Read)   - Default mode. Opens a file for reading. Throws error if file doesn't exist.
2. 'w' (Write)  - Opens a file for writing. CREATES the file if it doesn't exist. 
                  WARNING: OVERWRITES all existing data in the file!
3. 'a' (Append) - Opens a file for appending. Adds new data to the END of the file.
                  CREATES the file if it doesn't exist.
4. 'x' (Create) - Creates a specific file. Throws an error if the file already exists.
'''

'''
==============================================================================
2. WRITING AND CREATING A FILE ('w' mode)
Objective: Create a new text file and write data into it.
==============================================================================
'''
print("\n--- 2. Creating & Writing to a File ---")

# Step 1: Open the file in Write ('w') mode. 
# If "superman.txt" does not exist in your folder, Python creates it instantly.
file_w = open("superman.txt", "w")

# Step 2: Write content into the file.
file_w.write("Hello, this is Superman!\n")
file_w.write("This is Akarsh, and I am writing inside this file.\n")

# Step 3: ALWAYS close the file to save memory and finalize the write process.
file_w.close()
print("File 'superman.txt' created and written successfully.")


'''
==============================================================================
3. APPENDING TO A FILE ('a' mode)
Objective: Add new content to an existing file WITHOUT destroying the old data.
CRITICAL RULE: If you use 'w' again, the old text gets wiped out. Use 'a' to 
keep the old data safe.
==============================================================================
'''
print("\n--- 3. Appending to a File ---")

# Open the file in Append ('a') mode.
file_a = open("superman.txt", "a")

# Add new content to the very end of the file.
file_a.write("Now I am appending some new content inside the file.\n")

# Close the file
file_a.close()
print("New data appended successfully to 'superman.txt'.")


'''
==============================================================================
4. READING A FILE ('r' mode)
Objective: Extract data from a file and bring it into your Python program.
==============================================================================
'''
print("\n--- 4. Reading a File ---")

# Open the file in Read ('r') mode. (You can also just write open("superman.txt") 
# since 'r' is the default mode).
file_r = open("superman.txt", "r")

# Extract the entire content of the file and save it in a variable.
content = file_r.read()

# Print the extracted content to the terminal.
print("--- File Content Below ---")
print(content)
print("--------------------------")

# Close the file
file_r.close()


'''
==============================================================================
5. THE 'with' CONTEXT MANAGER (Best Practice)
Objective: Handle files safely without worrying about manually closing them.

CRITICAL RULE: If your code crashes before it reaches file.close(), the file 
might stay open in the background and corrupt data. 
Using the 'with' keyword automatically closes the file the exact moment 
the indentation block ends, even if errors occur!
==============================================================================
'''
print("\n--- 5. The 'with' Context Manager ---")

# Syntax: with open(path, mode) as variable_name:
with open("superman.txt", "r") as fs:
    
    # As long as we are indented, the file is open
    safe_content = fs.read()
    print("Successfully read using 'with open()':")
    print(safe_content.strip()) # .strip() removes trailing blank lines

# The moment we un-indent, 'superman.txt' is INSTANTLY and SAFELY closed!
# print(fs.read()) # This would throw a "ValueError: I/O operation on closed file."     