import sqlite3

db_path = '../data/users.db'

class DatabaseConnection:
    def __init__(self):
        self.conn = None
    
    def __enter__(self):
        self.conn = sqlite3.connect(db_path)
        return self.conn
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()
        return False

with DatabaseConnection() as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    for e in enumerate(users):
    	print(f"{e}")
