import pandas as pd
import joblib
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

print("\n--- Bias Analysis Report ---\n")

for attr in ["sex", "race"]:
    print(f"{attr.upper()}-based Selection Rates:")
    for group in df[attr].unique():
        rate = (df[df[attr] == group]["prediction"] == positive).mean()
        print(f"Group {group}: {round(rate,2)}")
    print()