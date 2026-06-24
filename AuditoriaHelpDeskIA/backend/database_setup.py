# backend/database_setup.py
import sqlite3

import os

DB_PATH = "data/tickets.db"

def setup_database():
    # Crear el directorio data si no existe
    os.makedirs("data", exist_ok=True)

def setup_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # ÚNICAMENTE creamos la tabla de tickets
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        status TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()
    print(f"Base de datos '{DB_PATH}' y tabla 'tickets' configuradas correctamente.")

if __name__ == "__main__":
    setup_database()