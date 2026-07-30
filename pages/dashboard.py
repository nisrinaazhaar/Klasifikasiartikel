import streamlit as st
from supabase import create_client
import pandas as pd

# =====================================
# TITLE
# =====================================

st.title("📊 Dashboard")

# =====================================
# DATABASE
# =====================================

url = "PROJECT_URL"
key = "ANON_KEY"

df = pd.read_sql_query(
    "SELECT * FROM articles",
    conn
)

conn.close()

# =====================================
# TOTAL ARTIKEL
# =====================================

st.metric(
    "Total Articles",
    len(df)
)

st.divider()

# =====================================
# HITUNG LABEL
# =====================================

computer_science = len(
    df[df["label"] == "Computer Science"]
)

medical = len(
    df[df["label"] == "Medical"]
)

economy = len(
    df[df["label"] == "Economy"]
)

# =====================================
# TAMPIL LABEL
# =====================================

st.subheader("Label Distribution")

col1, col2, col3 = st.columns(3)

# =====================================
# COMPUTER SCIENCE
# =====================================

with col1:

    st.info(
        f"""
        Computer Science
        
        Total Articles: {computer_science}
        """
    )

# =====================================
# MEDICAL
# =====================================

with col2:

    st.success(
        f"""
        Medical
        
        Total Articles: {medical}
        """
    )

# =====================================
# ECONOMY
# =====================================

with col3:

    st.warning(
        f"""
        Economy
        
        Total Articles: {economy}
        """
    )

# =====================================
# DATA TERBARU
# =====================================

st.divider()

st.subheader("📄 Latest Articles")

latest_df = df.sort_values(
    by="upload_time",
    ascending=False
).head(3)

for index, row in latest_df.iterrows():

    with st.container(border=True):

        st.write(f"### {row['title']}")

        if row["label"] == "Computer Science":
            st.info(row["label"])

        elif row["label"] == "Medical":
            st.success(row["label"])

        else:
            st.warning(row["label"])

        st.caption(
            f"Upload: {row['upload_time']}"
        )
