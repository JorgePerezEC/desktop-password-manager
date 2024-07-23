import pytest
from src.encryption.encryption import encrypt_password, decrypt_password

def test_encrypt_password():
    # Ejemplo de prueba para encriptar una contraseña
    password = "test_password"
    encrypted_password = encrypt_password(password)
    
    assert encrypted_password != password

# Pruebas a realizar:
# 1. Implementar una prueba (test) para verificar que la contraseña desencriptada es igual a la original (test_decrypt_password).
# 2. Implementar una prueba para verificar que una contraseña incorrecta no pasa la verificación (test_incorrect_password).

def test_decrypt_password():
    # Pista: Usa la función encrypt_password para encriptar y luego verifica usando decrypt_password
    pass

def test_incorrect_password():
    # Pista: Usa una contraseña incorrecta para verificar que decrypt_password no la acepta
    pass
