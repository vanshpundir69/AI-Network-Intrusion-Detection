# src/create_sample.py

import pandas as pd

df = pd.read_csv(
    "data/Wednesday-workingHours.pcap_ISCX.csv"
)

sample = df.sample(
    n=1000,
    random_state=42
)

sample.to_csv(
    "sample_data.csv",
    index=False
)

print("Sample dataset created!")