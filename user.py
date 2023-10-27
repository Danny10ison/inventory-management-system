
from database_setups import retrieve_from_database


def retrieve_users_from_database():
    return retrieve_from_database('users.json')


Users = retrieve_users_from_database()


# A function to get a user
def get_a_user(username_email):
    for user in Users:
        if user.get('username') == username_email:
            return user
        if user.get('email') == username_email:
            return user
    return False
