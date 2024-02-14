import random
import string
import hashlib
import time

# Password Generation Function
def generate_random_password(length=12):
    """Generate a random password with a mix of upper and lower case letters, digits, and special characters."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


