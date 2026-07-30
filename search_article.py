from supabase import create_client
import pandas as pd

def search_articles(keyword=""):

    url = "PROJECT_URL"
    key = "ANON_KEY"

   response = (
        supabase
        .table("articles")
        .select("*")
        .or_(f"title.ilike.%{keyword}%,label.ilike.%{keyword}%")
        .order("upload_time", desc=True)
        .execute()
    )
    
    df = pd.DataFrame(response.data)

    conn.close()

    return df
