from database_setups import save_to_database, retrieve_from_database

# A function check if user already register
def user_already_exists(user_list, username, email):
    for user in user_list:
        if user.get('username') == username:
            return True
        if user.get('email') == email:
            return True
    return False

# This function takes the user input and save the user to the database by excuting the "save_user_to_json_file" function
def register_user_from_input(user_list):
    name = input("Enter your name: ")
    username = input("Enter your username: ")
    email = input("Enter your email: ")

    if user_already_exists(user_list, username, email ):
         print("You are already registered, please login")
         return
    
    password = input("Enter your password: ")
    
    # Only "Customer" can register for security reason, "Manager" will be added manually to the database (the json file)
    new_user = {
        'name': name,
        'username': username,
        'email': email,
        'password': password,
        'role': 'Customer'
    }
    
    # Add the new user to the user list and save it
    user_list.append(new_user)
    save_to_database(user_list, 'users.json')
    print('Registration was successful')



def main():
    Users = []
    
    # Load existing users from JSON file (if it exists)
    try:
        Users = retrieve_from_database('users.json')
    except FileNotFoundError:
        pass
    
    register_user_from_input(Users)

 
    
if __name__ == "__main__":
    main()
