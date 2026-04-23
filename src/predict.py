import joblib
import pandas as pd

class FraudPredictor:
    def __init__(self, model_path):
        package = joblib.load(model_path)
        self.model = package["model"]
        self.scaler = package["scaler"]
        self.threshold = package["threshold"]

    def predict(self, df):
        df = df.copy()
        
        df[['Time','Amount']] = self.scaler.transform(df[['Time','Amount']])
        
        proba = self.model.predict_proba(df)[:,1]
        pred = (proba >= self.threshold).astype(int)
        
        return pred, proba