from argon2 import PasswordHasher

ph = PasswordHasher()

def encrypt_password(password):
    return ph.hash(password)

def decrypt_password(encrypted_password, password):
    try:
        if ph.verify(encrypted_password, password):
            return password
        else:
            return None
    except:
        return None
