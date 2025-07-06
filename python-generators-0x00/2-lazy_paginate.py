import mysql.connector
import time

def paginate_users(connection, page_size, offset):
    if not connection:
        return []
    
    users_page = []
    try:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT user_id, name, email, age FROM user_data LIMIT %s OFFSET %s"
        cursor.execute(query, (page_size, offset))
        users_page = cursor.fetchall()
        cursor.close()
    except mysql.connector.Error as e:
        print(f"Error paginating users: {e}")
    
    return users_page

def lazy_paginate(connection, page_size):
    offset = 0
    while True:
        print(f"Fetching page with size {page_size} at offset {offset}...")
        page = paginate_users(connection, page_size, offset)

        if not page:
            break
        
        yield page
        offset += page_size