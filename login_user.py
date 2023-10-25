from database_setups import retrieve_from_database

def login(username, password):
      # Load existing users from JSON file (if it exists)
    try:
        Users = retrieve_from_database('users.json')
    except FileNotFoundError:
        pass

    """function validates user
    """
    for user in Users:
        if user['username'] == username and user['password'] == password:
            return user  # Return the user information if credentials match
    return None  # Return None if no matching user is found