Caesar Cipher Cryptography Tool

A Python implementation of the Caesar cipher algorithm with encryption, decryption, and brute-force key recovery capabilities.

🔐 Features

Encryption
- Encrypts plaintext messages using a specified shift key (0-25)
- Preserves uppercase and lowercase formatting
- Maintains non-alphabetic characters (spaces, punctuation, numbers)

Decryption
- Decrypts ciphertext when the shift key is known
- Handles multi-paragraph encrypted texts

Brute-Force Key Recovery
- Automatically tests all 26 possible shift keys
- Displays preview of each decryption attempt
- Useful when the encryption key is unknown

 🛠️ Technologies Used
- Python
- Character encoding (ASCII/Unicode)
- Modular arithmetic

 🚀 How to Run
```bash
python caesar_cipher_code(Zakaria_Ghalmi).py
```

📖 How It Works

The Caesar cipher shifts each letter by a fixed number of positions in the alphabet:
- **Encryption**: Shifts letters forward (A → D with key 3)
- **Decryption**: Shifts letters backward (D → A with key 3)

 Functions:
- `encrypt(text, key)` - Encrypts plaintext with specified key
- `decrypt(text, key)` - Decrypts ciphertext with specified key

💡 Project Demonstrations

The code includes three practical examples:

1. Decryption with Known Key (key=8)
   - Demonstrates decrypting a message about transposition ciphers and grid systems

2. Encryption (key=15)
   - Encrypts a passage about cryptographic diffusion

3. Brute-Force Attack (key=21)
   - Tests all 26 possible keys on an encrypted passage about modern cryptography
   - Shows how weak encryption can be broken through exhaustive search

🎯 What This Demonstrates
- Understanding of classical cryptography
- String manipulation and character encoding in Python
- Algorithm implementation from scratch
- Vulnerability analysis (brute-force attacks)
- Why short keys and simple ciphers are insecure

 📝 Example Output
```
Encryption with key = 15:
Sxuujxdc btgktb ph p rdgctgbidct...

Testing all possible keys...
Key 0: Wlsjnialujbs uhx Yhwlsjncih...
Key 21: Cryptography and Encryption...
```


Zakaria Ghalmi

## 📚 Learning Outcomes
- Classical cipher algorithms
- Python string manipulation
- Modular arithmetic operations
- Cryptanalysis techniques
- Security implications of simple encryption schemes
