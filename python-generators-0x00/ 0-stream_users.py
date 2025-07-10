#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error

def stream_users():
    """Generator that yields user rows as dicts from MySQL DB one by one."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',           # replace with your MySQL username
            password='password',   # replace with your MySQL password
            database='ALX_prodev'
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")

        for row in cursor:
            yield row

        cursor.close()
        connection.close()
    except Error as e:
        print(f"Error streaming users: {e}")
        
