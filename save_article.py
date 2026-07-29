import sqlite3

def save_to_db(title, abstract, label, confidence, pdf_path):

    conn = sqlite3.connect("database/articles.db")

    cursor = conn.cursor()

    # =====================================
    # CEK DUPLIKAT
    # =====================================

    cursor.execute("""
    SELECT * FROM articles
    WHERE title = ?
    """, (title,))

    existing_article = cursor.fetchone()

    # =====================================
    # JIKA SUDAH ADA
    # =====================================

    if existing_article:

        conn.close()

        return False

    # =====================================
    # INSERT DATA
    # =====================================

    cursor.execute("""
    INSERT INTO articles
    (title, abstract, label, confidence, pdf_path)

    VALUES (?, ?, ?, ?, ?)
    """, (title, abstract, label, confidence, pdf_path))

    conn.commit()
    conn.close()

    return True