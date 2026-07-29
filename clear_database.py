import sqlite3

conn = sqlite3.connect("database/articles.db")

cursor = conn.cursor()

# hapus semua data
cursor.execute("DELETE FROM articles")

conn.commit()
conn.close()

print("Semua data berhasil dihapus 😭🔥")