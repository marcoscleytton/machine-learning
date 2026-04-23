from fastapi import FastAPI
import pandas as pd
from src.predict import FraudPredictor

app = FastAPI()

model = FraudPredictor("models/fraud_model.pkl")

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    pred, proba = model.predict(df)
    
    return {
        "fraude": int(pred[0]),
        "probabilidade": float(proba[0])
    }