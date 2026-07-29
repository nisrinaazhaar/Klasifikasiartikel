import pdfplumber
import re

def extract_abstract(pdf_path):

    text = ""

    # =====================================
    # EXTRACT TEXT FROM PDF
    # =====================================

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    # =====================================
    # CLEAN TEXT
    # =====================================

    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)

    # =====================================
    # ABSTRACT PATTERNS
    # =====================================

    patterns = [

        r"(?i)abstract\s*[:\-]?\s*(.*?)(?=keywords|index terms|introduction|1\.|i\.)",

        r"(?i)abstract\s*(.*?)(?=keyword|introduction)",

        r"(?i)summary\s*(.*?)(?=keywords|introduction)"
    ]

    abstract = ""

    # =====================================
    # TRY ALL PATTERNS
    # =====================================

    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            re.DOTALL
        )

        if match:

            abstract = match.group(1).strip()

            break

    if abstract == "":
        abstract = "Abstract not found."


    return abstract

