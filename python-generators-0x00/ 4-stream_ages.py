#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error

def stream_user_ages():
    """Generator that yields one user age at a time from the DB."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='ALX_prodev'
        )
        cursor = connection.cursor()
        cursor.execute("SELECT age FROM user_data")

        for (age,) in cursor:
            yield age

        cursor.close()
        connection.close()
    except Error as e:
        print(f"Error accessing database: {e}")


def compute_average_age():
    """Calculate average age using stream_user_ages generator."""
    total = 0
    count = 0
    for age in stream_user_ages():
        total += age
        count += 1

    if count > 0:
        average = total / count
        print(f"Average age of users: {average:.2f}")
    else:
        print("No users found.")
