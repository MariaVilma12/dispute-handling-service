import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="gokstad",
        database="dispute_management",
        port=3306
    )
