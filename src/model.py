from sklearn.linear_model import LogisticRegression

def train_model(X, y):
    model = LogisticRegression(C=0.01, max_iter=1000)
    model.fit(X, y)
    return model