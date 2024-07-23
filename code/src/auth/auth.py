import sqlite3
from src.encryption.encryption import encrypt_password
from sqlite3 import Error

def create_user(username, password, password_hint, master_password, pin):
    try:
        conn = sqlite3.connect('password_manager.db')
        cursor = conn.cursor()
        
        encrypted_password = encrypt_password(password)
        encrypted_master_password = encrypt_password(master_password)
        
        cursor.execute('''
            INSERT INTO tbl_user (username, password, password_hint, master_password, pin, state)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (username, encrypted_password, password_hint, encrypted_master_password, pin, True))
        
        conn.commit()
        conn.close()
        return True
    except Error as e:
        print(f"Error al crear el usuario: {e}")
        return False

def login(username, password):
    try:
        conn = sqlite3.connect('password_manager.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT password FROM tbl_user WHERE username = ? AND state = 1', (username,))
        result = cursor.fetchone()
        
        conn.close()
        
        if result:
            encrypted_password = result[0]
            if encrypt_password(password) == encrypted_password:
                return True
        return False
    except Error as e:
        print(f"Error al iniciar sesión: {e}")
        return False

# Pendiente de implementar
def logout(username):
    print(f"Usuario {username} ha cerrado sesión.")
