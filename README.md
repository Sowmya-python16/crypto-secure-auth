
# Cryptography, Key Management & Secure Auth

## Project Overview
This project demonstrates basic cryptographic operations using Python.

## Features
- AES-256-GCM encryption and decryption
- RSA-2048 digital signatures and verification
- bcrypt password hashing and verification

## Technologies Used
- Python
- cryptography
- bcrypt

## Installation
```bash
python -m pip install -r requirements.txt
```

## Run the Project
```bash
python main.py
```

## Security Best Practices
- Use a fresh random nonce for each AES-GCM encryption.
- Never expose private keys or passwords.
- Store real secrets securely outside source code.
- Plan key rotation and restrict access to keys.

## Disclaimer
This project is for educational and authorized testing purposes.
