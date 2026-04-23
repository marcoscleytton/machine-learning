import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from imblearn.under_sampling import RandomUnderSampler

# =========================
# 1. Carregar dados (Kaggle)
# =========================

df = pd.read_csv("creditcard.csv")

# =========================
# 2. Separar X e y
# =========================
X = df.drop("Class", axis=1)
y = df["Class"]

# =========================
# 3. Split
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# =========================
# 4. Normalização
# =========================
scaler = StandardScaler()

X_train[['Time','Amount']] = scaler.fit_transform(X_train[['Time','Amount']])
X_test[['Time','Amount']] = scaler.transform(X_test[['Time','Amount']])

# =========================
# 5. Balanceamento (RUS)
# =========================
rus = RandomUnderSampler(random_state=2)
X_train_rus, y_train_rus = rus.fit_resample(X_train, y_train)

# =========================
# 6. Modelo final
# =========================
model = LogisticRegression(C=0.01, max_iter=1000)
model.fit(X_train_rus, y_train_rus)

# =========================
# 7. Threshold final
# =========================
threshold = 0.85

# =========================
# 8. Salvar modelo (IMPORTANTE)
# =========================
model_package = {
    "model": model,
    "scaler": scaler,
    "threshold": threshold
}

joblib.dump(model_package, "models/fraud_model.pkl")

print("✅ Modelo salvo em models/fraud_model.pkl")