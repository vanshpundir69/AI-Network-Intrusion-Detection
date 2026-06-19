import pandas as pd

file_path = r"data/Wednesday-workingHours.pcap_ISCX.csv"

df = pd.read_csv(file_path)

print("Dataset Shape:")
print(df.shape)

print("\nFirst 10 Columns:")
print(df.columns[:10].tolist())

print("\nLabel Distribution:")
print(df[" Label"].value_counts())

print("\nFirst 5 Rows:")
print(df.head())