import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (change 'root' and 'password' as needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="yourpassword"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Ensure cursor and connection are closed
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Run the function
if __name__ == "__main__":
    create_database()

