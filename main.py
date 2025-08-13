"""
Project/File Name: ___________________________
Author:           ___________________________
Date Created:     ___________________________
Last Modified:    ___________________________

Purpose:          [Brief description of what this file/project does]

Dependencies:     [List any required libraries, modules, or files]
Usage:            [How to run or use this file/project]
Inputs:           [Describe expected input, if any]
Outputs:          [Describe output, if any]
Notes:            [Any additional important information]
"""

import sys  # Import the sys module for potential future use (not strictly needed here)

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract the second number from the first
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide the first number by the second
def divide(x, y):
    if y == 0:
        print("Error: Division by zero.")  # Handle division by zero
        return None
    return x / y

# Function to display the menu and get the user's operation choice
def get_operation():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    return input("Enter choice (1/2/3/4): ")

# Function to get two numbers from the user
def get_numbers():
    try:
        num1 = float(input("Enter first number: "))   # Convert input to float
        num2 = float(input("Enter second number: "))  # Convert input to float
        return num1, num2
    except ValueError:
        print("Invalid input. Please enter numbers.")  # Handle invalid input
        return get_numbers()  # Recursively ask again

# Main function to run the calculator loop
def main():
    while True:
        choice = get_operation()  # Get the user's operation choice
        if choice in ('1', '2', '3', '4'):
            num1, num2 = get_numbers()  # Get the two numbers from the user
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")  # Perform addition
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")  # Perform subtraction
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")  # Perform multiplication
            elif choice == '4':
                result = divide(num1, num2)  # Perform division
                if result is not None:
                    print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid choice.")  # Handle invalid menu choice

        # Ask the user if they want to perform another calculation
        next_calc = input("Do you want to perform another calculation? (yes/no): ")
        if next_calc.lower() != 'yes':
            print("Goodbye!")  # Exit message
            break  # Exit the loop and end the program

# This ensures the main function runs only if the script is executed directly
if __name__ == "__main__":
    main()