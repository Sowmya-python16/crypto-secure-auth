
from os import urandom

import bcrypt
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


# 1. AES-256-GCM Encryption and Decryption
print("===== AES-256-GCM =====")

# Generate a secure 256-bit key
key = AESGCM.generate_key(bit_length=256)

# Generate a fresh random 12-byte nonce
nonce = urandom(12)

message = b"Hello, this is a demo secret message!"

# Encrypt the message
aes = AESGCM(key)
encrypted = aes.encrypt(nonce, message, None)

# Decrypt the message
decrypted = aes.decrypt(nonce, encrypted, None)

print("Original message:", message.decode())
print("Encrypted successfully!")
print("Decrypted message:", decrypted.decode())
print(
    "Encryption/Decryption:",
    "PASS" if decrypted == message else "FAIL"
)


# 2. RSA-2048 Digital Signature Verification
print("\n===== RSA-2048 DIGITAL SIGNATURE =====")

# Generate RSA public and private keys
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# Sign the message using the private key
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Verify the signature using the public key
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature verification: PASS")
except Exception:
    print("Signature verification: FAIL")


# 3. bcrypt Password Hashing
print("\n===== BCRYPT PASSWORD HASHING =====")

# Demo password only; never use this as a real password
password = b"Demo-Only-Password-123!"

# Hash password with a random salt
password_hash = bcrypt.hashpw(
    password,
    bcrypt.gensalt(rounds=12)
)

print("Password hash created successfully.")

# Check correct password
correct = bcrypt.checkpw(password, password_hash)
print("Correct password check:", "PASS" if correct else "FAIL")

# Check incorrect password
wrong = bcrypt.checkpw(b"wrong-password", password_hash)
print("Wrong password rejected:", "PASS" if not wrong else "FAIL")


print("\n===== ALL DEMO TESTS COMPLETED =====")
