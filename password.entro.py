import random
import string
import hashlib
import time

# Password Generation Function
def generate_random_password(length=12):
    """Generate a random password with a mix of upper and lower case letters, digits, and special characters."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# BIP39 Passphrase Generation Function
def generate_bip39_passphrase(word_list, num_words=12):
    """Generate a random passphrase using the BIP39 wordlist."""
    return ' '.join(random.choice(word_list) for _ in range(num_words))
    
