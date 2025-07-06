import mysql.connector

DB_CONFIG = {
    'host': 'localhost',
    'user': 'varsath',
    'password': 'varsath',
    'port': 3306
}
DB_NAME = 'ALX_prodev'

def stream_users():
    connection = mysql.connector.connect(**DB_CONFIG, database=DB_NAME)
    try:
        cursor = connection.cursor(buffered=True)
        cursor.execute("SELECT user_id, name, email, age FROM user_data")
        for row in cursor:
            yield row

        cursor.close()
    except mysql.connector.Error as e:
        print(f"Error streaming data: {e}")
        