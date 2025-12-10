import pandas as pd
from src.model_utils import load_model

def prepare_input(data: dict):
    """
    Make the JSON input match EXACT training column names + order.
    """

    # Fix mismatched column name: API sends Year_Built, model expects Year Built
    data["Year Built"] = data.pop("Year_Built")

    # Convert to DataFrame
    df = pd.DataFrame([data])

    # Create Property_Age exactly like training
    df["Property_Age"] = df["Sold_Year"] - df["Year Built"]

    # FINAL training feature order
    final_columns = [
        "Location",
        "Size",
        "Bedrooms",
        "Bathrooms",
        "Year Built",
        "Condition",
        "Type",          # ← MUST BE INCLUDED
        "Sold_Year",
        "Sold_Month",
        "Property_Age"
    ]

    df = df[final_columns]
    return df


def predict_price(input_data: dict):
    """
    Load saved XGBoost model and return predicted price.
    """
    model = load_model()
    df = prepare_input(input_data)
    prediction = model.predict(df)[0]
    return round(float(prediction), 2)
