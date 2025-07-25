import sqlite3
import functools
from datetime import datetime

#### decorator to log SQL queries

def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query', args[0] if args else None)
        print(f"[{datetime.now()}] - Executing query: \"{query}\"\n")
        with open('queries.log', 'a') as log_file:
            log_file.write(f"[{datetime.now()}] - Executed query: \"{query}\"\n")
        return func(*args, **kwargs)
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('../data/users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
