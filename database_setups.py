import json
import os

# This function saves the registered users to a json file user (to mimics a database)
# It takes 2 option:
#   1. The users to save in the database
#   2. The filename, the name of the json file or we can call it the "database name"


def save_to_database(data, database_filename):
    # Create the 'database' folder if it doesn't exist
    if not os.path.exists('database'):
        os.mkdir('database')
    with open("database/" + database_filename, 'w') as json_file:
        return json.dump(data, json_file, indent=4)


# This function retrieves or get the data from json file or database (to mimic a database)
def retrieve_from_database(database_filename):
    # First check to get the data, retun an empty array in case it can't get the data
    try:
        with open("database/" + database_filename, 'r') as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        return []
