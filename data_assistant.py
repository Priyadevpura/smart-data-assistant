import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
import time

st.set_page_config(page_title="Smart Data Assistant", layout="wide")

st.title("📊 Smart Data Assistant")
st.write("Upload your CSV file, ask questions, and explore insights with charts!")

uploaded_file = st.file_uploader("📁 Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("📄 Data Preview")
    st.dataframe(df)

    st.subheader("ℹ️ Basic Info")
    st.write(f"Rows: {df.shape[0]} | Columns: {df.shape[1]}")
    st.write("Columns:", list(df.columns))

    # Chatbox
    st.subheader("💬 Ask a Question (Mock AI)")
    user_question = st.text_input("Ask something like 'What is the trend of sales?'")

    if user_question:
        with st.spinner("Thinking..."):
            time.sleep(2)
            mock_responses = [
                "Based on your data, Q2 shows the highest growth.",
                "Sales are consistently higher on weekends.",
                "Customer churn rate is lowest in the South region.",
                "The average order value is $34.56.",
                "The most popular product is Category A."
            ]
            st.success("✅ Mock AI Answer:")
            st.write(random.choice(mock_responses))

    # Charts Section
    st.subheader("📊 Visual Insights")

    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    if numeric_columns:
        selected_col = st.selectbox("Choose a column to visualize", numeric_columns)

        if selected_col:
            st.write(f"Histogram of `{selected_col}`")
            fig, ax = plt.subplots()
            sns.histplot(df[selected_col], kde=True, ax=ax)
            st.pyplot(fig)

            st.write(f"Top 10 values in `{selected_col}`")
            st.bar_chart(df[selected_col].value_counts().head(10))

        if st.button("📈 Show Correlation Heatmap"):
            corr = df.corr(numeric_only=True)
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)
    else:
        st.info("No numeric columns available for visualization.")
