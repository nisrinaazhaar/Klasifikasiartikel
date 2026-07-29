import sqlite3
import pandas as pd

def search_articles(keyword=""):

    conn = sqlite3.connect("database/articles.db")

    query = """
    SELECT * FROM articles
    WHERE title LIKE ?
    OR label LIKE ?
    ORDER BY upload_time DESC
    """

    df = pd.read_sql_query(
        query,
        conn,
        params=(f"%{keyword}%", f"%{keyword}%")
    )

    conn.close()

    return df