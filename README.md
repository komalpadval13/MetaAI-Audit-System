MetaAI Audit System

This project is an AI auditing system that checks machine learning models for bias, fairness, ethical risk, explainability, and data leakage. The goal is to ensure that AI models are not only accurate but also fair and responsible.

The project uses a trained machine learning model and evaluates its behavior using Responsible AI principles.

--------------------------------------------------

Project Features

- Bias analysis based on gender and race
- Fairness evaluation using the 80% Disparate Impact Rule
- Ethical AI risk scoring
- Explainable AI using feature importance
- Data leakage and proxy risk detection
- Final audit report for deployment readiness

--------------------------------------------------

Project Structure

audit/  
  bias_analysis.py  
  fairness_analysis.py  
  ethical_score.py  
  explainability.py  
  leakage_detection.py  

data/  
  adult.csv  

model/  
  trained_model.pkl  

report/  
  generate_report.py  

app.py  
train_model.py  
requirements.txt  

--------------------------------------------------

Dataset

The project uses the UCI Adult Income Dataset.  
The task is to predict whether a person earns more than 50K per year.

Sensitive attributes used for auditing:
- Gender (sex)
- Race (race)

--------------------------------------------------

Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Random Forest Classifier
- Git and GitHub

--------------------------------------------------

How to Run the Project

1. Install dependencies  
   pip install -r requirements.txt

2. Train the model  
   python train_model.py

3. Run the AI audit  
   python app.py

--------------------------------------------------

Output Summary

- Bias detected in gender and race
- Fairness violations identified
- Ethical AI score generated
- Explainable features reported
- Final verdict indicates mitigation is required

--------------------------------------------------

Conclusion

This project shows that high accuracy does not guarantee fair or ethical AI.  
AI systems must be audited before real-world deployment to ensure responsible usage.

--------------------------------------------------

Author

Komal Padval  
GitHub: https://github.com/komalpadval13/MetaAI-Audit-System
