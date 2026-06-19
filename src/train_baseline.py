import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

print("Loading dataset...")

# Load dataset
df = pd.read_csv(
    r"data/Wednesday-workingHours.pcap_ISCX.csv"
)

print("Original Shape:", df.shape)

# Remove duplicates
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

print("\nLabel Distribution:")
print(df[" Label"].value_counts())

# Features and Target
X = df.drop(columns=[" Label"])
y = df[" Label"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining Model...")

# Random Forest Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

# Train
model.fit(X_train, y_train)

print("Model Trained Successfully!")

# Save Model
joblib.dump(
    model,
    "saved_models/random_forest_model.pkl"
)

print("Model Saved Successfully!")

# Predictions
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(
    y_test,
    predictions
)

print("\nAccuracy:", accuracy)

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        predictions
    )
)

# Top Features
feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nTop 15 Important Features:")
print(feature_importance.head(15))