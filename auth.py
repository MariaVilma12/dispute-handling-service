import hashlib
from dat import get_connection

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(name, role, username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (name, role, username, password) VALUES (%s, %s, %s, %s)",
        (name, role, username, hash_password(password))
    )
    conn.commit()
    conn.close()

def login(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT user_id, name, role FROM users WHERE username=%s AND password=%s",
        (username, hash_password(password))
    )
    user = cursor.fetchone()
    conn.close()
    return user
