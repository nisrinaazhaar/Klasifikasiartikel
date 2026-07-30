from supabase import create_client
import pandas as pd

def search_articles(keyword=""):

    url = "https://jjmxqradekqclhbteplw.supabase.co"
    key = "sb_publishable_InNUNhB1KvsnsGhxJET8cQ_iUHX8uUg"

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
