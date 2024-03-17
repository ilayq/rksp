from cryptography.fernet import Fernet


token_key = Fernet.generate_key()
f = Fernet(token_key)
