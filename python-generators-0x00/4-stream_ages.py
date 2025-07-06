import mysql.connector
from decimal import Decimal

DB_CONFIG = {
    'host': 'localhost',
    'user': 'varsath',
    'password': 'varsath',
    'port': 3306
}
DB_NAME = 'ALX_prodev'

def stream_user_ages():
    connection = mysql.connector.connect(**DB_CONFIG, database=DB_NAME)
    if not connection:
        print("Error: No database connection provided.")
        return

    try:
        cursor = connection.cursor(buffered=True)
        cursor.execute("SELECT age FROM user_data")

        for (age,) in cursor:
            yield age
        
        cursor.close()
    except mysql.connector.Error as e:
        print(f"Error streaming user ages: {e}")


def calculate_average_age(connection):
    age_generator = stream_user_ages(connection)
    
    total_age = Decimal('0.0')
    user_count = 0

    for age in age_generator:
        if age is not None:
            total_age += age
            user_count += 1
    
    if user_count > 0:
        average_age = total_age / user_count
        print(f"Average age of users: {average_age:.2f}")
    else:
        print("No users found or ages are all NULL, cannot calculate average.")
