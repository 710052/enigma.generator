# Secure Password and Passphrase Generator

This project provides a Python-based solution for generating secure passwords and BIP39 passphrases. It incorporates best practices in security, including the use of external entropy for enhanced randomness and a simple strength checker for generated passwords.

## Features

- **Random Password Generation**: Generates strong passwords with a mix of upper and lower case letters, digits, and special characters.
- **BIP39 Passphrase Generation**: Creates secure passphrases using the BIP39 wordlist, suitable for cryptographic applications.
- **Password Strength Checker**: Offers a basic assessment of password strength based on length and character diversity.
- **External Entropy**: Conceptual implementation for enhancing randomness using system or user-generated events.

## Installation

To run this project, you'll need Python installed on your system. This project was developed with Python 3.8+, but it should be compatible with other versions that support the used libraries.

1. Clone the repository:

```bash
git clone https://yourrepositorylink.com
```

2. Navigate to the project directory:

```bash
cd secure-password-generator
```

3. (Optional) It's recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

4. Install the required libraries:
