"""
app/security.py
Encrypt/decrypt Gmail app passwords before they touch the database.
Generate the key ONCE and store it in an env var — losing it means
every stored app password becomes unrecoverable, so back it up safely
(not in git).

    python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
"""
import os
from cryptography.fernet import Fernet

_fernet = Fernet(os.environ["ENCRYPTION_KEY"].encode())


def encrypt_value(plain_text: str) -> str:
    return _fernet.encrypt(plain_text.encode()).decode()


def decrypt_value(encrypted_text: str) -> str:
    return _fernet.decrypt(encrypted_text.encode()).decode()
