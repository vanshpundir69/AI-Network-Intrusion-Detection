import pandas as pd
import numpy as np

file_path = r"data/Wednesday-workingHours.pcap_ISCX.csv"

print("Loading dataset...")
df = pd.read_csv(file_path)

print("Original Shape:", df.shape)

# Remove duplicate rows
df = df.drop_duplicates()

# Replace infinite values
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# Remove missing values
df.dropna(inplace=True)

print("After Cleaning:", df.shape)

# Convert labels
df[" Label"] = df[" Label"].apply(
    lambda x: 0 if x == "BENIGN" else 1
)

print("\nLabel Counts:")
print(df[" Label"].value_counts())

print("\nDataset Ready!")python