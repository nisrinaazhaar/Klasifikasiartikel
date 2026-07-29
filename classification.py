import streamlit as st
import pandas as pd
import os

from extract_pdf import extract_abstract
from predict import predict_article
from save_article import save_to_db

# =====================================
# CONFIG
# =====================================

st.set_page_config(
    page_title="Klasifikasi Artikel Ilmiah",
    layout="wide"
)

# =====================================
# FOLDER UPLOAD
# =====================================

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# =====================================
# TITLE
# =====================================

st.title("📚 Scientific Article Classification System")

st.write("""
This system is specifically designed for English scientific articles 
and supports topic classification in the fields of Computer Science, 
Economy, and Medical using a BERT-based model.

Upload a scientific article in PDF format, and the system will 
automatically extract the abstract and classify the article topic.
""")

st.divider()

# =====================================
# INPUT TITLE
# =====================================

title = st.text_input(
    "Enter Article Title"
)

# =====================================
# UPLOAD PDF
# =====================================

uploaded_file = st.file_uploader(
    "Upload PDF File",
    type=["pdf"]
)

# =====================================
# BUTTON
# =====================================

if st.button("🔍 Classify Article"):

    if uploaded_file is None:

        st.error("Please upload a PDF file first")

    elif title == "":

        st.error("Please enter the article title")

    else:

        with st.spinner("Processing article..."):

            # =================================
            # SAVE PDF
            # =================================

            pdf_path = os.path.join(
                UPLOAD_FOLDER,
                uploaded_file.name
            )

            with open(pdf_path, "wb") as f:
                f.write(uploaded_file.read())

            # =================================
            # EXTRACT ABSTRACT
            # =================================

            abstract = extract_abstract(pdf_path)

            # =================================
            # COMBINE TEXT
            # =================================

            combined_text = title + " " + abstract

            # =================================
            # PREDICTION
            # =================================

            label, confidence, all_scores = predict_article(
                combined_text
            )

            # =================================
            # SAVE DATABASE
            # =================================

            saved = save_to_db(
                title,
                abstract,
                label,
                float(confidence),
                pdf_path
            )

        # =====================================
        # SUCCESS
        # =====================================

        st.success(
            "Classification completed successfully"
        )

        st.subheader("Classification Result")

        # =====================================
        # LABEL WARNA
        # =====================================

        if label == "Computer Science":
            st.info(label)

        elif label == "Medical":
            st.success(label)

        else:
            st.warning(label)

        # =====================================
        # CONFIDENCE
        # =====================================

        confidence_percent = round(
            confidence * 100,
            2
        )

        st.write(
            f"Confidence: {confidence_percent}%"
        )

        st.progress(float(confidence))

        st.subheader("Confidence Scores")

        labels = [
            "Computer Science",
            "Economy",
            "Medical"
        ]

        for lbl, score in zip(labels, all_scores):

            st.write(
                f"{lbl}: {round(score * 100, 2)}%"
            )

        chart_df = pd.DataFrame({

            "Category": [
                "Computer Science",
                "Economy",
                "Medical"
            ],

            "Confidence": [
                all_scores[0] * 100,
                all_scores[1] * 100,
                all_scores[2] * 100
            ]
        })

        st.subheader(
            "Classification Confidence Distribution"
        )

        st.bar_chart(
            chart_df,
            x="Category",
            y="Confidence"
        )