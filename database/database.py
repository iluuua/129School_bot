from pathlib import Path
import datetime
import sqlite3

path = Path(__file__).parent / 'db.sqlite'


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(f'{path}', check_same_thread=False)

    def create_tables(self):
        cursor = self.connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS USER
            (
                user_id INT PRIMARY KEY,
                username TEXT NOT NULL,
                coins INTEGER NOT NULL
            );
        """)
        self.connection.commit()
        cursor.close()

    def add_user(self, user_id, username):
        cursor = self.connection.cursor()
        cursor.execute("""
        INSERT INTO USER (user_id, username, coins)
        VALUES (?, ?, ?)
        """, (user_id, username, 0))
        self.connection.commit()
        cursor.close()

    def check_registration(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT 1 FROM USER WHERE user_id = ?", (user_id,))
        result = cursor.fetchone()
        cursor.close()
        return bool(result)

    def update_balance(self, user_id, balance):
        cursor = self.connection.cursor()
        cursor.execute("""
        UPDATE USER SET coins = ? WHERE user_id = ?
        """, (balance, user_id,))
        self.connection.commit()
        cursor.close()

    def get_balance(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("""
        SELECT coins FROM USER WHERE user_id = ?
        """, (user_id,))
        result = cursor.fetchone()
        cursor.close()
        return result[0]

    def get_stats(self):
        pass

