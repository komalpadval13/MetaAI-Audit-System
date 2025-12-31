import joblib
import pandas as pd
import os

BASE = os.path.dirname(os.path.dirname(__file__))

model = joblib.load(os.path.join(BASE, "model/trained_model.pkl"))

importance = model.feature_importances_
features = model.feature_names_in_

df = pd.DataFrame({
    "Feature": features,
    "Importance": importance
}).sort_values(by="Importance", ascending=False)

print("\n--- Explainability Report (Top 10 Features) ---\n")
print(df.head(10))