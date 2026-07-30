from supabase import create_client

def save_to_db(title, abstract, label, confidence, pdf_path):

    url = "PROJECT_URL"
    key = "ANON_KEY"

    supabase = create_client(url, key)

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

    supabase.table("articles").insert({
        "title": title,
        "abstract": abstract,
        "label": label,
        "confidence": confidence,
        "pdf_path": pdf,
    }).execute()
    conn.close()

    return True
