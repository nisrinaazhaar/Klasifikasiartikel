from supabase import create_client
import pandas as pd

def search_articles(keyword=""):

    url = "PROJECT_URL"
    key = "ANON_KEY"

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
