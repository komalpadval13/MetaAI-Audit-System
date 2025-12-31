import os

os.system("python audit/bias_analysis.py")
os.system("python audit/fairness_analysis.py")
os.system("python audit/ethical_score.py")
os.system("python audit/explainability.py")
os.system("python audit/leakage_detection.py")
os.system("python report/generate_report.py")