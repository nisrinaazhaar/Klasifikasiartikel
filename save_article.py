from supabase import create_client

def save_to_db(title, abstract, label, confidence, pdf_path):

    url = "https://jjmxqradekqclhbteplw.supabase.co"
    key = "sb_publishable_InNUNhB1KvsnsGhxJET8cQ_iUHX8uUg"

    supabase = create_client(url, key)

    # =====================================
    # CEK DUPLIKAT
    # =====================================

    response = (
        supabase
        .table("articles")
        .select("*")
        .eq("title", title)
        .execute()
    )
    
    existing_article = response.data

    # =====================================
    # JIKA SUDAH ADA
    # =====================================

    if existing_article:

        conn.close()

        return False

    # =====================================
    # INSERT DATA
    # =====================================

    supabase.table("articles").insert({
        "title": title,
        "abstract": abstract,
        "label": label,
        "confidence": confidence,
        "pdf_path": pdf,
    }).execute()
    conn.close()

    return True
