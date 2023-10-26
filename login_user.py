from database_setups import retrieve_from_database


def login(username, password):

    Users = retrieve_from_database('users.json')

    """function validates user
    """
    for user in Users:
        if user['username'] == username and user['password'] == password:
            return user  # Return the user information if credentials match
    return None  # Return None if no matching user is found
