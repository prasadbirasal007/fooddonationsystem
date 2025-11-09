# test_conn.py
import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='donor_user',
        password='DonorPass123!',
        database='food_donation'
    )
    print("Connected:", conn.is_connected())
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM donations")
    print("Rows:", cur.fetchone()[0])
    cur.close()
    conn.close()
except Error as e:
    print("Error:", e)
