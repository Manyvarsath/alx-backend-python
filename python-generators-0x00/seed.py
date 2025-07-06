import mysql.connector
import csv
import os
import uuid

DB_CONFIG = {
    'host': 'localhost',
    'user': 'varsath',
    'password': 'varsath',
    'port': 3306
}
DB_NAME = 'ALX_prodev'

def connect_db():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            return connection
    except mysql.connector.Error as e:
        return None

def create_database(connection):
    if not connection:
        return
    try:
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        cursor.close()
    except mysql.connector.Error as e:
        print(f"Error creating database: {e}")

def connect_to_prodev():
    try:
        config = DB_CONFIG.copy()
        config['database'] = DB_NAME
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            return connection
    except mysql.connector.Error as e:
        return None

def create_table(connection):
    if not connection:
        return
    try:
        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL(5, 2) NOT NULL,
            INDEX(user_id)
        )
        """
        cursor.execute(create_table_query)
        cursor.close()
    except mysql.connector.Error as e:
        print(f"Error creating table: {e}")

def insert_data(connection, data):
    if not connection:
        return
    try:
        cursor = connection.cursor()
        insert_query = """
        INSERT INTO user_data (user_id, name, email, age)
        VALUES (%s, %s, %s, %s)
        """
        check_query = "SELECT email FROM user_data WHERE email = %s"

        for row in data:
            cursor.execute(check_query, (row['email'],))
            if cursor.fetchone():
                continue

            user_uuid = str(uuid.uuid4())
            user_values = (user_uuid, row['name'], row['email'], row['age'])
            cursor.execute(insert_query, user_values)

        connection.commit()
        cursor.close()
    except mysql.connector.Error as e:
        print(f"Error inserting data: {e}")
