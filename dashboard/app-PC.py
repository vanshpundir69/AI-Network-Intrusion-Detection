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

st.write(
    "Upload a network traffic CSV file for intrusion detection."
)

uploaded_file = st.file_uploader(
    "Choose CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    try:
        # Load CSV
        df = pd.read_csv(uploaded_file)

        st.success("Dataset Uploaded Successfully!")

        st.write("Dataset Shape:", df.shape)

        st.subheader("Dataset Preview")
        st.dataframe(df.head())

        # Load model
        model = joblib.load(
            "saved_models/random_forest_model.pkl"
        )

        # Remove label column if present
        if " Label" in df.columns:
            df = df.drop(columns=[" Label"])

        # Predictions
        predictions = model.predict(df)

        attack_count = np.sum(predictions == 1)
        benign_count = np.sum(predictions == 0)

        st.subheader("Detection Results")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Total Records",
            len(predictions)
        )

        col2.metric(
            "Benign",
            benign_count
        )

        col3.metric(
            "Attack",
            attack_count
        )

        # Prediction dataframe
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

    except Exception as e:
        st.error(f"Error: {str(e)}")