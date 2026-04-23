import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(df, scaler=None, fit=False):
    df = df.copy()
    
    if fit:
        scaler = StandardScaler()
        df[['Time','Amount']] = scaler.fit_transform(df[['Time','Amount']])
        return df, scaler
    else:
        df[['Time','Amount']] = scaler.transform(df[['Time','Amount']])
        return df