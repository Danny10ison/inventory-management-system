#!/bin/python3
""" CLI based inventory management system
"""

from login_user import login
from product import add_product, view_products, view_single_product
from request import request_for_a_product, approve_or_decline_a_request
import getpass

display_message = """
Welcome to Inventory Management Application
By: Serverless Sorcerers
"""
print(display_message)


def manager_menu():
    """fucntion to display manager menu
    """
    while True:
        manager_options = """
        Manager Menu:
        1. View Inventory (display all available items)
        2. Add Item (add new inventory)
        3. View a single item/product
        4. View all request
        5. View a single request
        6. Approve or decline a request
        7. Remove Item (Remove item from inventory to a user, based on request)
        8. Exit (close the app)
        """
        print(manager_options)

        choice = input("Enter your choice: ")

        if choice == '1':
            # View Inventory
            print("Viewing Inventory...")
            view_products()
        elif choice == '2':
            # Add Item
            print("Adding an item...")
            add_product()
        elif choice == '3':
            # Remove Item
            print("Viewing an item...")
            view_single_product()
        elif choice == '4':
            # Remove Item
            print("Removing an item...")
        elif choice == '5':
            # Remove Item
            print("Removing an item...")
        elif choice == '6':
            # Remove Item
            approve_or_decline_a_request()
        elif choice == '8':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-4).")


def customer_menu(logged_in_user):
    """fucntion to display manager menu
    """
    while True:
        customer_options = """
        Customer Menu:
        1. View Inventory (display all available items)
        2. View a single item/product
        3. Request an item/product
        4. Exit (close the app)
        """
        print(customer_options)

        choice = input("Enter your choice: ")

        if choice == '1':
            # View Inventory
            print("Viewing Inventory...")
            view_products()
        elif choice == '2':
            # Add Item
            print("Viewing an item...")
            view_single_product()
        elif choice == '3':
            # Remove Item
            print("Adding an item...")
            request_for_a_product(logged_in_user)
        elif choice == '4':
            # Remove Item
            print("Removing an item...")
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-4).")


# Main app runner
while True:
    display_options = """
    1. Login
    0. Exit App
    """
    print(display_options)

    choice = input("Enter your choice: ")

    if choice == '1':
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")

        logged_in_user = login(username, password)
        if logged_in_user:
            if logged_in_user['role'] == 'Manager':
                print("Login successful. Welcome, {}! Your role is {}.".format(
                    logged_in_user['name'], logged_in_user['role']))
                manager_menu()  # Call the manager's menu

            if logged_in_user['role'] == 'Customer':
                print("Login successful. Welcome, {}! ".format(
                    logged_in_user['name']))
                customer_menu(logged_in_user)  # Call the customer's menu

        else:
            print("Invalid username or password. Please try again.")
    elif choice == '0':
        print("Exiting the app. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter '1' to login or '0' to exit.")
