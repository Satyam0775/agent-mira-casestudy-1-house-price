import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os

# FIXED IMPORT – MUST use src.config
from src.config import RAW_DATA_PATH, PROCESSED_DATA_PATH


def preprocess_data():
    print("Loading dataset from:", RAW_DATA_PATH)

    # Load raw Excel file
    df = pd.read_excel(RAW_DATA_PATH)

    # Handle missing values
    df.fillna(df.median(numeric_only=True), inplace=True)
    df.fillna("Unknown", inplace=True)

    # Convert Date Sold
    df["Date Sold"] = pd.to_datetime(df["Date Sold"], errors="coerce")
    df["Sold_Year"] = df["Date Sold"].dt.year
    df["Sold_Month"] = df["Date Sold"].dt.month

    # Create Age feature
    df["Property_Age"] = df["Sold_Year"] - df["Year Built"]

    # Encode categorical columns
    encoder = LabelEncoder()
    for col in ["Location", "Condition", "Type"]:
        df[col] = encoder.fit_transform(df[col].astype(str))

    # Drop unused columns
    df.drop(["Property ID", "Date Sold"], axis=1, inplace=True)

    # Ensure artifacts folder exists
    os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)

    # Save processed CSV
    df.to_csv(PROCESSED_DATA_PATH, index=False)

    print("\n✔ Processed data saved at:")
    print(PROCESSED_DATA_PATH)

    return df


if __name__ == "__main__":
    preprocess_data()
