import sqlite3

db_path = '../data/users.db'

query = "SELECT * FROM users WHERE age > ?"
params = (25,)

class ExecuteQuery:
    def __init__(self):
        self.query = query
        self.params = params
        self.cursor = None 
        self.conn = None
    
    def __enter__(self):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query, self.params)
        return self.cursor.fetchall()

    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()
        return False

with ExecuteQuery() as executedQuery:
    results = executedQuery
    for i, user in enumerate(results):
        print(f"User {i+1}: {user}")


