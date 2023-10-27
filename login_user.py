from database_setups import retrieve_from_database
import getpass
from utils import verify_password


Users = retrieve_from_database('users.json')


def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    """function validates user
    """
    for user in Users:
        if user["username"] == username:
            hashed_password = user["password"]
            if verify_password(password, hashed_password):
                print('Login')
                return user  # Return the user information if credentials match

    print('Failed')
    return None  # Return None if no matching user is found
