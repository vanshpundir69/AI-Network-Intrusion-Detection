import streamlit as st

st.set_page_config(
    page_title="AI Network Intrusion Detection",
    layout="wide"
)

st.title("🛡️ AI Network Intrusion Detection System")

st.success("Random Forest Model Loaded")

st.metric(
    label="Model Accuracy",
    value="99.93%"
)

st.metric(
    label="Dataset",
    value="CIC-IDS2017"
)

st.metric(
    label="Records Processed",
    value="610,492"
)

st.write("---")

st.subheader("Project Overview")

st.write("""
This project detects malicious network traffic using
Machine Learning trained on the CIC-IDS2017 dataset.

Attack Types:
- DoS Hulk
- DoS GoldenEye
- DoS Slowloris
- DoS Slowhttptest
- Heartbleed

Model:
- Random Forest Classifier
""")