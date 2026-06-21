import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px

st.set_page_config(
    page_title="AI Network Intrusion Detection",
    layout="wide"
)

st.title("🛡️ AI Network Intrusion Detection System")

# Day 3 Dashboard Metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Model", "Random Forest")
col2.metric("Accuracy", "99.93%")
col3.metric("Dataset", "CIC-IDS2017")
col4.metric("Features", "78")

st.write("---")

uploaded_file = st.file_uploader(
    "Upload Network Traffic CSV",
    type=["csv"]
)

if uploaded_file is not None:

    try:
        df = pd.read_csv(uploaded_file)

        st.success("Dataset Uploaded Successfully!")

        st.write("Dataset Shape:", df.shape)

        st.subheader("Dataset Preview")
        st.dataframe(df.head())

        model = joblib.load(
            "saved_models/random_forest_model.pkl"
        )

        if " Label" in df.columns:
            df = df.drop(columns=[" Label"])

        predictions = model.predict(df)

        attack_count = np.sum(predictions == 1)
        benign_count = np.sum(predictions == 0)

        st.subheader("Detection Results")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Total Records",
            len(predictions)
        )

        c2.metric(
            "Benign",
            benign_count
        )

        c3.metric(
            "Attack",
            attack_count
        )

        result_df = pd.DataFrame({
            "Prediction": predictions
        })

        result_df["Prediction"] = result_df[
            "Prediction"
        ].map({
            0: "BENIGN",
            1: "ATTACK"
        })

        st.subheader("Predictions")

        st.dataframe(result_df.head(20))

        # Pie Chart
        chart_data = pd.DataFrame({
            "Category": ["BENIGN", "ATTACK"],
            "Count": [benign_count, attack_count]
        })

        fig = px.pie(
            chart_data,
            values="Count",
            names="Category",
            title="Network Traffic Distribution"
        )

        st.plotly_chart(fig)

        # Download Button
        csv = result_df.to_csv(index=False)

        st.download_button(
            label="Download Predictions",
            data=csv,
            file_name="predictions.csv",
            mime="text/csv"
        )

        # Day 3 Feature Importance
        importance_df = pd.read_csv(
            "feature_importance.csv"
        )

        st.subheader(
            "Top 10 Important Features"
        )

        st.bar_chart(
            importance_df.head(10).set_index("Feature")
        )

    except Exception as e:
        st.error(f"Error: {str(e)}")