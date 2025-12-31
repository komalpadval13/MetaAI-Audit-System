import pandas as pd
import joblib
import numpy as np
import os

BASE = os.path.dirname(os.path.dirname(__file__))

df = pd.read_csv(os.path.join(BASE, "data/adult.csv"))
df.replace(" ?", pd.NA, inplace=True)
df.dropna(inplace=True)

model = joblib.load(os.path.join(BASE, "model/trained_model.pkl"))

X = pd.get_dummies(df.drop("income", axis=1))
X = X.reindex(columns=model.feature_names_in_, fill_value=0)

df["prediction"] = model.predict(X)
positive = model.classes_[1]

def selection_rate(g):
    return np.mean(g["prediction"] == positive)

def disparate_impact(rates):
    if max(rates) == 0:
        return 0
    return min(rates) / max(rates)

print("\n--- FAIRNESS ANALYSIS REPORT ---\n")

for attr in ["sex", "race"]:
    print(f"Fairness Analysis for: {attr.upper()}")
    rates = []

    for group in df[attr].unique():
        r = selection_rate(df[df[attr] == group])
        rates.append(r)
        print(f"  Group {group} → Selection Rate: {round(r,2)}")

    di = disparate_impact(rates)
    print("  Disparate Impact Ratio:", round(di, 2))

    if di < 0.8:
        print("  ❌ UNFAIR (Bias Detected)")
    else:
        print("  ✅ FAIR")

    print("-" * 40)