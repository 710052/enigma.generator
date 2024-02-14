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
The script assumes the presence of certain libraries for optional features, such as external entropy collection, QR code generation, and cryptographic operations. While the core functionality (password and passphrase generation) doesn't require external libraries, here are some you might consider for extending the project:

- `pynput` for capturing keyboard and mouse events for external entropy.
- `pyperclip` for clipboard operations (note: this was conceptual and not included in the final script).
- `qrcode` for generating QR codes of passwords/passphrases.
- Cryptographic libraries such as `bitcoinlib` for Bitcoin mnemonic generation or equivalent libraries for Monero.

```bash
pip install pynput pyperclip qrcode bitcoinlib
```
## Usage

Run the script from the command line:

```bash
python secure_password_generator.py
```
Follow the on-screen prompts to generate a password or passphrase. For additional functionalities, such as integrating with cryptographic libraries for Bitcoin and Monero mnemonic generation or implementing Shamir's Secret Sharing, you will need to extend the script with the respective libraries.

## Security Considerations

- **External Entropy**: The conceptual implementation for external entropy is a placeholder. Actual deployment should ensure robust collection mechanisms that do not compromise user security.
- **Cryptographic Use**: For generating mnemonics for cryptocurrencies or implementing secret sharing schemes, ensure you use well-reviewed libraries and follow best practices in cryptographic security.
- **Data Storage**: If implementing export functionalities for storing passwords or passphrases, use secure storage practices, potentially including encryption.
