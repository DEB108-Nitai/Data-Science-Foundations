'''
==============================================================================
PYTHON COMPLETE NOTES: FILE HANDLING C.R.U.D PROJECT 🚀
(Based on the Sheryians AI School Full Python Course)
==============================================================================
'''

'''
==============================================================================
1. PROJECT ARCHITECTURE & OBJECTIVE
Objective: Create a CLI application that performs C.R.U.D operations 
(Create, Read, Update, Delete) directly on FILES inside a directory.

Instead of affecting the entire operating system, this project safely targets 
only the current folder where the script is running.

Modules Used:
- pathlib: A modern, object-oriented way to handle file paths.
- os: Used for interacting directly with the operating system (like deleting files).
==============================================================================
'''

import os
from pathlib import Path

# ==============================================================================
# 2. HELPER FUNCTION: SHOW ALL FILES
# Objective: Show the user what files already exist before they perform an action.
# ==============================================================================
def read_file_and_folder():
    print("\n--- Current Directory Contents ---")
    
    # Path("") targets the current working directory
    current_path = Path("") 
    
    # rglob("*") recursively finds all files and folders in this path
    # We convert it to a list to iterate through it easily
    items = list(current_path.rglob("*"))
    
    # enumerate() gives us both the index (i) and the value (item)
    # We use i+1 so the list displayed to the user starts at 1 instead of 0
    for i, item in enumerate(items):
        print(f"{i + 1}. {item}")
    print("----------------------------------\n")


# ==============================================================================
# 3. CREATE OPERATION
# ==============================================================================
def create_file():
    read_file_and_folder()
    
    name = input("Please tell your file name (e.g., hello.txt): ")
    p = Path(name)
    
    # Validation: Ensure the file doesn't already exist
    if not p.exists():
        try:
            # Open in Write ('w') mode to create the file
            with open(p, "w") as fs:
                data = input("What do you want to write in this file? \n> ")
                fs.write(data)
            print(f"\nSuccess: File '{name}' created successfully!")
        except Exception as err:
            print(f"\nAn error occurred: {err}")
    else:
        print(f"\nError: The file '{name}' already exists.")


# ==============================================================================
# 4. READ OPERATION
# ==============================================================================
def read_file():
    read_file_and_folder()
    
    name = input("Which file do you want to read? ")
    p = Path(name)
    
    # Validation: Ensure the path exists AND it is a file (not a folder)
    if p.exists() and p.is_file():
        try:
            # Open in Read ('r') mode
            with open(p, "r") as fs:
                data = fs.read()
            print(f"\n--- Content of {name} ---")
            print(data)
            print("-------------------------")
            print("Read successfully.")
        except Exception as err:
            print(f"\nAn error occurred: {err}")
    else:
        print("\nError: No such file exists, or it is a directory.")


# ==============================================================================
# 5. UPDATE OPERATION
# Objective: Give the user 3 specific ways to update an existing file.
# ==============================================================================
def update_file():
    read_file_and_folder()
    
    name = input("Which file do you want to update? ")
    p = Path(name)
    
    if p.exists() and p.is_file():
        print("\nPress 1 for changing the name of your file.")
        print("Press 2 for overwriting the data of your file.")
        print("Press 3 for appending data to your file.")
        
        try:
            response = int(input("Tell your response (1/2/3): "))
        except ValueError:
            print("\nError: Please enter a valid number.")
            return

        try:
            # Option 1: Rename the file
            if response == 1:
                new_name = input("Tell your new file name: ")
                p2 = Path(new_name)
                p.rename(p2) # pathlib's built-in rename method
                print(f"\nSuccess: File renamed to '{new_name}'.")
                
            # Option 2: Overwrite the data ('w' mode)
            elif response == 2:
                with open(p, "w") as fs:
                    data = input("What do you want to write? (This will overwrite existing data):\n> ")
                    fs.write(data)
                print("\nSuccess: Data overwritten.")
                
            # Option 3: Append new data ('a' mode)
            elif response == 3:
                with open(p, "a") as fs:
                    data = input("What do you want to append?\n> ")
                    # Adding a space before the new data to keep it clean
                    fs.write(" " + data) 
                print("\nSuccess: Data appended.")
                
            else:
                print("\nError: Invalid option selected.")
                
        except Exception as err:
            print(f"\nAn error occurred: {err}")
            
    else:
        print("\nError: No such file exists, or it is a directory.")


# ==============================================================================
# 6. DELETE OPERATION
# ==============================================================================
def delete_file():
    read_file_and_folder()
    
    name = input("Which file do you want to delete? ")
    p = Path(name)
    
    if p.exists() and p.is_file():
        try:
            # Using the 'os' module to remove the file
            os.remove(name)
            print(f"\nSuccess: File '{name}' removed successfully.")
        except Exception as err:
            print(f"\nAn error occurred: {err}")
    else:
        print("\nError: No such file exists, or it is a directory.")


# ==============================================================================
# 7. MAIN EXECUTION (CLI INTERFACE)
# ==============================================================================

# A while loop keeps the CLI running until the user decides to exit
while True:
    print("\n=========================================")
    print("      FILE HANDLING C.R.U.D SYSTEM       ")
    print("=========================================")
    print("1. Create a file")
    print("2. Read a file")
    print("3. Update a file")
    print("4. Delete a file")
    print("5. Exit")
    
    try:
        check = int(input("\nPlease tell your response (1-5): "))
    except ValueError:
        print("\nError: Invalid input! Please enter a number.")
        continue

    # Logic Routing based on user input
    if check == 1:
        create_file()
    elif check == 2:
        read_file()
    elif check == 3:
        update_file()
    elif check == 4:
        delete_file()
    elif check == 5:
        print("\nExiting program. Goodbye!")
        break
    else:
        print("\nError: Invalid option! Please select between 1 and 5.")