import pandas as pd
import os

BASE = os.path.dirname(os.path.dirname(__file__))

df = pd.read_csv(os.path.join(BASE, "data/adult.csv"))

print("\n--- Data Leakage Detection ---\n")

if "income" in df.columns:
    print("Target column detected properly")

high_corr = df.corr(numeric_only=True)["hours_per_week"].abs().max()

if high_corr > 0.9:
    print("⚠️ Possible leakage detected")
else:
    print("✅ No strong leakage detected")