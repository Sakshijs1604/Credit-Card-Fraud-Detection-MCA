import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="fraud_detection_db"
    )


def check_login(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT * FROM admins
        WHERE username = %s AND password = %s
    """

    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result is not None


def save_prediction(amount, prediction, probability):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO prediction_history
        (transaction_time, amount, prediction, fraud_probability)
        VALUES (NOW(), %s, %s, %s)
    """

    cursor.execute(
        query,
        (amount, prediction, probability)
    )

    conn.commit()

    cursor.close()
    conn.close()


def get_history():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT history_id,
               transaction_time,
               amount,
               prediction,
               fraud_probability
        FROM prediction_history
        ORDER BY history_id DESC
    """

    cursor.execute(query)
    records = cursor.fetchall()

    cursor.close()
    conn.close()

    return records


def delete_history(history_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM prediction_history WHERE history_id = %s",
        (history_id,)
    )

    conn.commit()

    cursor.close()
    conn.close()
