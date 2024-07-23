import sqlite3
from sqlite3 import Error

# Initialize database
def create_db():
    conn = sqlite3.connect('password_manager.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS tbl_user (
                        id INTEGER PRIMARY KEY,
                        username NVARCHAR(255) NOT NULL,
                        password NVARCHAR(255) NOT NULL,
                        password_hint NVARCHAR(255) NOT NULL,
                        master_password NVARCHAR(255) NOT NULL,
                        profile_photo BLOB,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        pin NVARCHAR(255) NOT NULL,
                        state BOOLEAN NOT NULL
                      )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS tbl_category (
                        id INTEGER PRIMARY KEY,
                        name NVARCHAR(255) NOT NULL,
                        icon BLOB,
                        user_id INTEGER NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        state BOOLEAN NOT NULL,
                        FOREIGN KEY (user_id) REFERENCES tbl_user (id)
                      )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS tbl_folder (
                        id INTEGER PRIMARY KEY,
                        name NVARCHAR(255) NOT NULL,
                        folder_color NVARCHAR(255),
                        user_id INTEGER NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        state BOOLEAN NOT NULL,
                        FOREIGN KEY (user_id) REFERENCES tbl_user (id)
                      )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS tbl_password (
                        id INTEGER PRIMARY KEY,
                        website NVARCHAR(255) NOT NULL,
                        username_or_email NVARCHAR(255) NOT NULL,
                        password NVARCHAR(255) NOT NULL,
                        icon BLOB,
                        category_id INTEGER,
                        folder_id INTEGER,
                        user_id INTEGER NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        state BOOLEAN NOT NULL,
                        FOREIGN KEY (user_id) REFERENCES tbl_user (id),
                        FOREIGN KEY (category_id) REFERENCES tbl_category (id),
                        FOREIGN KEY (folder_id) REFERENCES tbl_folder (id)
                      )''')
    
    conn.commit()
    conn.close()

def get_passwords_by_category(category_id):
    try:
        conn = sqlite3.connect('password_manager.db')
        cursor = conn.cursor()

        cursor.execute('''
                SELECT * FROM tbl_password
                WHERE category_id = ? AND state = 1
                       ''', (category_id,))
        
        passwords = cursor.fetchall()
        conn.close()
        return passwords
    except Error as err:
        print(f"Error trying to get passwords: {e}")
        return []
    
def get_passwords_by_folder(folder_id):
    try:
        conn = sqlite3.connect('password_manager.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM tbl_password
            WHERE folder_id = ? AND state = 1
        ''', (folder_id,))
        
        passwords = cursor.fetchall()
        conn.close()
        return passwords
    except Error as e:
        print(f"Error al obtener contraseñas por carpeta: {e}")
        return []
    
if __name__ == "__main__":
    create_db()
