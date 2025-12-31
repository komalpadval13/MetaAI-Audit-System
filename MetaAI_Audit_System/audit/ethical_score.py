bias_penalty = 30
fairness_penalty = 30
explainability_bonus = 20
leakage_penalty = 10

ethical_score = 100 - bias_penalty - fairness_penalty - leakage_penalty + explainability_bonus

print("\n--- Ethical AI Score ---")
print("Ethical Score:", ethical_score, "/ 100")

if ethical_score < 60:
    print("Risk Level: HIGH")
elif ethical_score < 80:
    print("Risk Level: MEDIUM")
else:
    print("Risk Level: LOW")