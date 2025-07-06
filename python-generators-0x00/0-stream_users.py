import mysql.connector

def stream_users(connection):
    if not connection:
        return

    try:
        cursor = connection.cursor(buffered=True)
        cursor.execute("SELECT user_id, name, email, age FROM user_data")
        for row in cursor:
            yield row

        cursor.close()
    except mysql.connector.Error as e:
        print(f"Error streaming data: {e}")
        