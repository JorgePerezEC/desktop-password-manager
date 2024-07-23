import sqlite3

conn = sqlite3.connect(':memory:')
print("Conexión a SQLite establecida")
conn.close()
