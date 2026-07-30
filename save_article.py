from supabase import create_client

def save_to_db(title, abstract, label, confidence, pdf_path):

    url = "https://jjmxqradekqclhbteplw.supabase.co"
    key = "sb_publishable_InNUNhB1KvsnsGhxJET8cQ_iUHX8uUg"

    supabase = create_client(url, key)

    try:

        response = (
            supabase
            .table("articles")
            .select("*")
            .eq("title", title)
            .execute()
        )

        print("SELECT:", response.data)

        if response.data:
            return False

        result = (
            supabase
            .table("articles")
            .insert({
                "title": title,
                "abstract": abstract,
                "label": label,
                "confidence": confidence,
                "pdf_path": pdf_path,
            })
            .execute()
        )

        print("INSERT:", result)

        return True

    except Exception as e:
        print("ERROR ASLI:", repr(e))
        raise
