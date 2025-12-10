from fastapi import FastAPI
from pydantic import BaseModel

# Import prediction function
from src.predict import predict_price


app = FastAPI(title="House Price Prediction API")


# Input schema (UPDATED → Type is REQUIRED)
class Property(BaseModel):
    Location: int
    Size: float
    Bedrooms: int
    Bathrooms: int
    Year_Built: int
    Condition: int
    Type: int          # MUST INCLUDE THIS
    Sold_Year: int
    Sold_Month: int


@app.get("/")
def root():
    return {"message": "House Price Prediction API is running!"}


@app.post("/predict")
def predict(data: Property):
    prediction = predict_price(data.dict())
    return {"predicted_price": prediction}
