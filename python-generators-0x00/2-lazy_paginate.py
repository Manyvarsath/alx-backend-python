import mysql.connector
import time

DB_CONFIG = {
    'host': 'localhost',
    'user': 'varsath',
    'password': 'varsath',
    'port': 3306
}
DB_NAME = 'ALX_prodev'

def paginate_users(connection, page_size, offset):
    if not connection:
        return []
    
    users_page = []
    try:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM user_data LIMIT %s OFFSET %s"
        cursor.execute(query, (page_size, offset))
        users_page = cursor.fetchall()
        cursor.close()
    except mysql.connector.Error as e:
        print(f"Error paginating users: {e}")
    
    return users_page

def lazy_paginate(page_size, offset=0):
    connection = mysql.connector.connect(**DB_CONFIG, database=DB_NAME)
    while True:
        print(f"Fetching page with size {page_size} at offset {offset}...")
        page = paginate_users(connection, page_size, offset)

        if not page:
            break
        
        yield page
        offset += page_size