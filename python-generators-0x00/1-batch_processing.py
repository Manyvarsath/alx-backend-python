import mysql.connector
from decimal import Decimal

def stream_users_in_batches(connection, batch_size=10):
    if not connection:
        return

    try:
        cursor = connection.cursor(buffered=True)
        cursor.execute("SELECT user_id, name, email, age FROM user_data")
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch

        cursor.close()
    except mysql.connector.Error as e:
        print(f"Error streaming data in batches: {e}")

def batch_processing(connection, batch_size=10):
    user_batches_generator = stream_users_in_batches(connection, batch_size)
    for i, batch in enumerate(user_batches_generator):
        print(f"\n--- Processing Batch {i + 1} ---")
        found_in_batch = False
        for user in batch:
            user_age = user[3]
            if isinstance(user_age, Decimal) and user_age > 25:
                found_in_batch = True
                print(f"  - Found user over 25: {user[1]} (Age: {user_age})")
        
        if not found_in_batch:
            print("  - No users over 25 in this batch.")

