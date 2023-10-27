import random
import bcrypt


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
