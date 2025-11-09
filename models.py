# models.py
import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    'host': '127.0.0.1',
    'user': 'donor_user',
    'password': 'DonorPass123!',
    'database': 'food_donation'
}

def get_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print('Error connecting to MySQL:', e)
        raise

def init_db():
    # simple connectivity test; will raise if connection fails
    conn = get_connection()
    conn.close()

def add_donation(donor_name, contact, quantity, pickup_address, notes):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''INSERT INTO donations
             (donor_name, contact, quantity, pickup_address, notes)
             VALUES (%s,%s,%s,%s,%s)'''
    cursor.execute(sql, (donor_name, contact, quantity, pickup_address, notes))
    conn.commit()
    inserted_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return inserted_id

def get_all_donations():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM donations ORDER BY created_at DESC')
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def delete_donation(donation_id):
    """
    Delete a donation row by id.
    Returns True if a row was deleted, False otherwise.
    """
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM donations WHERE id = %s"
    cursor.execute(sql, (donation_id,))
    conn.commit()
    deleted = cursor.rowcount  # number of rows affected
    cursor.close()
    conn.close()
    return deleted > 0
