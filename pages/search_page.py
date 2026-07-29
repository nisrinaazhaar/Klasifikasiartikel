import streamlit as st
import os

from search_article import search_articles

# =====================================
# PAGE TITLE
# =====================================

st.title("Search Scientific Articles")

# =====================================
# SEARCH INPUT
# =====================================

keyword = st.text_input(
    "Search by Title or Label"
)

# =====================================
# AMBIL DATA
# =====================================

df = search_articles(keyword)

st.write(f"Total Articles: {len(df)}")

st.divider()

# =====================================
# TAMPILKAN ARTIKEL
# =====================================

for index, row in df.iterrows():

    with st.container(border=True):

        # =================================
        # TITLE
        # =================================

        st.subheader(row["title"])

        # =================================
        # UPLOAD TIME
        # =================================

        st.caption(
            f"Upload Time: {row['upload_time']}"
        )

        # =================================
        # LABEL
        # =================================

        st.write("### Classification Result")

        if row["label"] == "Computer Science":
            st.info(row["label"])

        elif row["label"] == "Medical":
            st.success(row["label"])

        else:
            st.warning(row["label"])

        # =================================
        # CONFIDENCE
        # =================================

        confidence_percent = round(
            row["confidence"] * 100,
            2
        )

        st.write(
            f"Confidence: {confidence_percent}%"
        )

        st.progress(float(row["confidence"]))


        # =================================
        # PDF BUTTON
        # =================================

        pdf_path = row["pdf_path"]

        if os.path.exists(pdf_path):

            with open(pdf_path, "rb") as pdf_file:

                st.download_button(
                    label="📥 Download PDF",
                    data=pdf_file,
                    file_name=os.path.basename(pdf_path),
                    mime="application/pdf",
                    key=index
                )

    st.divider()
