from dat import get_connection

def list_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, name, role FROM users")
    users = cursor.fetchall()
    conn.close()
    return users
