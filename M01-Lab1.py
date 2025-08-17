"""
Project/File Name: Food Menu
Author:           Marc Robertson
Date Created:     08/15/2025
Last Modified:    08/17/2025

Purpose:          [This program takes the input from users from the menu, using the dictionary to give each item a key. Once selected it will be added to a total_cost function which will be displayed once the loop is returned."]

Dependencies:     [List any required libraries, modules, or files.]
Usage:            [Run code, input the necessary data in terminal, watch the program do its magic.]
Inputs:           [Customers are presented with an initial name input, then expected to input a number from the menu, or "done" if not wanting to proceed with ordering.]
Outputs:          [Outputs should vary, should display an initial welcome message, greeting with a custom menu, error message if invalid number is entered, or a confirmation message when item is added to the tota cost. Lastly, an order total is printed in the end.]
Notes:            [Any additional important information]
"""

# Directions for programming
"""
START
Display a welcome message to the customer
Define a menu with food items and their prices (e.g., Burger - $5, Pizza - $8, Salad - $4, Soda - $2)
Initialize total order amount to 0
LOOP (repeat until the customer is done ordering):
    Display the menu with item numbers and prices
    Ask the customer to enter the item number they want to order
    Ask the customer to enter the quantity for that item
    Calculate the cost for this item:
    item cost = price of item * quantity
    Add the item cost to the total order amount
    Ask the customer if they want to order another item (yes/no)
    IF the answer is "no":
        Exit the loop
Display the total order amount to the customer
Display a thank you message
END
"""

# Dictionary using array to index the list for the menu; the item number is the key which contains item name and price 

menu = {

    1: {"name": "Burger", "price": 7},
    2: {"name": "Hotdog", "price": 3},
    3: {"name": "Drink", "price": 2},
    4: {"name": "Cake", "price": 5},
    5: {"name": "Pizza", "price": 5}
    
}

# Initialize variable

order_total = 0 

#Print welcome message to user

name = input("Welcome to Marc's Food Shop! Can I have a name for the order? ")
print(f"Welcome {name}, what can I get started for you? \n") 

# Print menu frin array 

for item_num, item_info in menu.items():
    print(f"Item #{item_num}: {item_info['name']} - ${item_info['price']}.00")

print("\nType the item number to order, or type 'done' if you've changed your mind.\n")

# While loop while True to continue to continue asking for item number

while True:
    choice = input("Enter item number: ")

# Ends the loop if user inputs "done"

    if choice == "done":
        break

# Otherwise the item number choice is input, the value is stored as an integer in the variable choice && the choice is added to the order total. 
    if choice.isdigit():
        choice = int(choice)
        if choice in menu:
            order_total += menu[choice]["price"]
            print(f"Added {menu[choice]['name']} to your order. Current total: ${order_total}.00")

# Edge case scenario where incorrect type of response is inputted. 
        else: 
            print("Invalid item number, please try another menu number.")

    else:
        print("Please enter a valid number or 'done'. ")

# Prints the final total from the menu choices throughout the while loop

print(f"\nThanks {name}! Your order total is: ${order_total}.00")