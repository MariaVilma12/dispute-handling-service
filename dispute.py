from dat import get_connection

def create_dispute(title, description):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO disputes (title, description, status) VALUES (%s, %s, %s)",
        (title, description, "Open")
    )
    conn.commit()
    conn.close()

def assign_dispute(dispute_id, user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE disputes SET assigned_to=%s WHERE dispute_id=%s",
        (user_id, dispute_id)
    )
    conn.commit()
    conn.close()

def update_status(dispute_id, status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE disputes SET status=%s WHERE dispute_id=%s",
        (status, dispute_id)
    )
    conn.commit()
    conn.close()

def list_disputes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT d.dispute_id, d.title, d.status, u.name
        FROM disputes d
        LEFT JOIN users u ON d.assigned_to = u.user_id
    """)
    disputes = cursor.fetchall()
    conn.close()
    return disputes
