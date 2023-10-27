import random
import bcrypt
import string


# Generate a random 5-digit number
def generate_random_number_for_id():
    return str(random.randint(10000, 99999))


# Function to hash a password during registration
def hash_password(password):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


# Function to verify a password during login
def verify_password(entered_password, hashed_password):
    return bcrypt.checkpw(entered_password.encode('utf-8'), hashed_password.encode('utf-8'))


def generate_strong_password(length=12):
    # Define character sets for each category
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = "!@#$%^&*()_-+=<>?/[]{}|"

    # Combine all character sets
    all_characters = lowercase_letters + \
        uppercase_letters + digits + special_characters

    # Ensure the password is at least 12 characters long
    if length < 12:
        length = 12

    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password
