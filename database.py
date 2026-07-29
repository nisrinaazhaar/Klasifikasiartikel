import sqlite3

conn = sqlite3.connect("database/articles.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS articles (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    title TEXT,

    abstract TEXT,

    label TEXT,

    confidence REAL,

    pdf_path TEXT,

    upload_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("Database berhasil dibuat 😭🔥")