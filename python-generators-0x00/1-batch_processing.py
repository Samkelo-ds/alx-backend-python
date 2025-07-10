#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error

def stream_users_in_batches(batch_size):
"""Generator that yields batches of users from the database."""
try:
connection = mysql.connector.connect(
host='localhost',
user='root',
 password='password',
 database='ALX_prodev'
)
cursor = connection.cursor(dictionary=True)
cursor.execute("SELECT * FROM user_data")

while True:
batch = cursor.fetchmany(batch_size)
if not batch:
break
yield batch

cursor.close()
 connection.close()
except Error as e:
print(f"Database error: {e}")

def batch_processing(batch_size):
"""Process each batch by filtering users over the age of 25."""
for batch in stream_users_in_batches(batch_size):
for user in batch:
if user['age'] > 25:
yield user  # This line makes it a generator
