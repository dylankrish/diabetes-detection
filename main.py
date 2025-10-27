# IMPORTANT: FOR EDUCATIONAL USE ONLY! 
# Not for clinical use or to diagnose, treat, cure, or prevent any disease.
# -----


import os
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)
apimodel = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")

SYSTEM_PROMPT = (
"You are a careful, evidence-aware health triage assistant. "
"You DO NOT diagnose. You estimate relative risk based on provided metrics, "
"explain the reasoning succinctly, and give practical next steps. "
"Be conservative about any urgent advice."
)

# ask questions
age = input("Enter age: ")
sex = input("Enter gender: ")
bmi = input("Enter BMI: ")
fpg = input("Enter Fasting plasma glucose (FPG): ")
hba1c = input("Enter HBA1C: ")
bp = input("Enter Systolic BP: ")
familyhistory = input("Does your family have any history of diabetes (yes/no): ")
polyuria = input("Frequent urination (polyuria) (yes/no): ")
polydipsia = input("Excessive thirst (polydipsia) (yes/no): ")
gestational = input("Prior gestational diabetes (if applicable) (yes/no): ")
activity_days = input("Physical activity (days/week ≥30 min): ")



USER_PROMPT = (
"Using the inputs below, estimate relative risk for diabetes and give a diagnosis to the user.\n"
"with keys: risk_level (low|moderate|high), probability_percent (0-100), rationale, recommended_actions (array), red_flags (array).\n\n"
"Inputs:\n"
"- Age: {age} years\n"
"- Sex: {sex}\n"
"- BMI: {bmi}\n"
"- Fasting plasma glucose (FPG): {fpg} mg/dL\n"
"- HbA1c: {hba1c} %\n"
"- Systolic BP: {sbp} mmHg\n"
"- Family history of diabetes (first-degree relative): {family_history}\n"
"- Frequent urination (polyuria): {polyuria}\n"
"- Excessive thirst (polydipsia): {polydipsia}\n"
"- Prior gestational diabetes (if applicable): {gestational}\n"
"- Physical activity (days/week ≥30 min): {activity_days}\n\n"
"Important: Keep explanations short. Include any red flags that warrant prompt care (e.g., very high glucose,\n"
"unintended weight loss, altered mental status)."
)

response = client.chat.completions.create(
    model=apimodel,
    messages=[
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": USER_PROMPT},
    ]
)
response = response.choices[0].message.content
print(response)