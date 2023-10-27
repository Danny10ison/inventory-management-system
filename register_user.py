from database_setups import save_to_database, retrieve_from_database
from utils import hash_password, generate_strong_password
import getpass
import re


Users = retrieve_from_database('users.json')


# A function check if user already register
def user_already_exists(username, email):
    for user in Users:
        if user.get('username') == username:
            return True
        if user.get('email') == email:
            return True
    return False


# This function takes the user input and save the user to the database by excuting the "save_user_to_json_file" function
def register():
    name = input("Enter your name: ")
    username = input("Enter your username: ")
    email = input("Enter your email: ")

    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        print("You entered an invalid email")
        return

    if user_already_exists(username, email):
        print("You are already registered, please login")
        return

    password_options = """
    Password options:
    1. Generate a strong password
    2. Enter your own password
    """

    print(password_options)

    choice = int(input("Enter your request option: "))

    if choice == 1:
        password = generate_strong_password(16)
    elif choice == 2:
        password = getpass.getpass(
            "Enter your password (At least 8 characters): ")

        if len(password) < 8:
            print('Your password must be at least 8 characters')
            return
    else:
        print("Invalid choice. Please enter a valid option (1-2).")

    # Only "Customer" can register for security reason, "Manager" will be added manually to the database (the json file)
    new_user = {
        'name': name,
        'username': username,
        'email': email,
        # Convert the hashed bytes password to string
        'password': hash_password(password).decode('utf-8'),
        'role': 'Customer'
    }

    # Add the new user to the user list and save it
    Users.append(new_user)
    save_to_database(Users, 'users.json')

    # Save the credentials in a credentials.text file
    credentials = f"Username: {username}\nEmail: {email}\nPassword: {password}\n "
    with open("credentials.txt", 'a') as credentials_file:
        credentials_file.write(credentials)

    print('Registration was successful! Try logging in to the portal')
    print('Your credeentials has been saved in a credentials.text file')


def main():

    register()


if __name__ == "__main__":
    main()
