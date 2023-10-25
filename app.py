#!/bin/python3
""" CLI based inventory management system
"""

display_message = """
Welcome to Inventory Management Application
By: Serverless Sorcerers
"""
print(display_message)

# Sample user data for the porject
Users = [
    {
        'name': 'Daniel Osei',
        'username': 'DOsei',
        'email': 'daniel@gmail.com',
        'role': 'Manager',
        'password': 'd1234567'
    },
    {
        'name': 'John Doe',
        'username': 'JDoe',
        'email': 'johndoe@gmail.com',
        'role': 'Customer',
        'password': 'd1234567'
    },
    {
        'name': 'Sarah Freeman',
        'username': 'Safman',
        'email': 'sarahfman@gmail.com',
        'role': 'Customer',
        'password': 'd1234567'
    }
]

def login(username, password):
    """function validates user
    """
    for user in Users:
        if user['username'] == username and user['password'] == password:
            return user  # Return the user information if credentials match
    return None  # Return None if no matching user is found

def manager_menu():
    """fucntion to display manager menu
    """
    while True:
        manager_options = """
        Manager Menu:
        1. View Inventory (display all available items)
        2. Add Item (add new inventory)
        3. Remove Item (Remove item from inventory to a user, based on request)
        4. Exit (close the app)
        """
        print(manager_options)

        choice = input("Enter your choice: ")

        if choice == '1':
            # View Inventory
            print("Viewing Inventory...")
        elif choice == '2':
            # Add Item
            print("Adding an item...")
        elif choice == '3':
            # Remove Item
            print("Removing an item...")
        elif choice == '4':
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
        password = input("Enter your password: ")
        
        logged_in_user = login(username, password)
        if logged_in_user:
            if logged_in_user['role'] == 'Manager':
                print("Login successful. Welcome, {}! Your role is {}.".format(logged_in_user['name'], logged_in_user['role']))
                manager_menu()  # Call the manager's menu
            else:
                print("Login successful. Welcome, {}! Your role is {}.".format(logged_in_user['name'], logged_in_user['role']))
        else:
            print("Invalid username or password. Please try again.")
    elif choice == '0':
        print("Exiting the app. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter '1' to login or '0' to exit.")
