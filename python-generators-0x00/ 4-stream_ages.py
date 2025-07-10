#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error

def stream_user_ages():
    """Generator that yields one user age at a time from the DB."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',           # Replace if needed
            password='password',   # Replace if needed
            database='ALX_prodev'
        )
        cursor = connection.cursor()
        cursor.execute("SELECT age FROM user_data")

        for (age,) in cursor:
            yield age

        cursor.close()
        connection.close()
    except Error as e:
        print(f"Error: {e}")
        
