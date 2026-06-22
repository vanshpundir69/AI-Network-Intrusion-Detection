import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

df = pd.read_csv(
    "data/Wednesday-workingHours.pcap_ISCX.csv"
)

df = df.drop_duplicates()
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)

df[" Label"] = df[" Label"].apply(
    lambda x: 0 if x == "BENIGN" else 1
)

X = df.drop(columns=[" Label"])
y = df[" Label"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = joblib.load(
    "saved_models/random_forest_model.pkl"
)

predictions = model.predict(X_test)

cm = confusion_matrix(
    y_test,
    predictions
)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm
)

disp.plot()

plt.savefig(
    "screenshots/confusion_matrix.png",
    bbox_inches="tight"
)

print("Confusion Matrix Saved!")