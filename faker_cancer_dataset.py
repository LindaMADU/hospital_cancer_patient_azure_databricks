import pandas as pd
import random
from faker import Faker

fake = Faker()
Faker.seed(42)
random.seed(42)

N = 600

cancer_types = [
    "Breast Cancer",
    "Lung Cancer",
    "Colorectal Cancer",
    "Prostate Cancer",
    "Leukemia",
    "Skin Cancer",
    "Bladder Cancer",
    "Kidney Cancer",
    "Thyroid Cancer",
    "Lymphoma",
    "Pancreatic Cancer",
    "Cervical Cancer",
]

cancer_weights = [0.15, 0.12, 0.10, 0.09, 0.08, 0.08, 0.07, 0.07, 0.07, 0.07, 0.05, 0.05]

stage_weights_map = {
    "Breast Cancer":     [0.25, 0.30, 0.25, 0.20],
    "Lung Cancer":       [0.10, 0.20, 0.35, 0.35],
    "Colorectal Cancer": [0.20, 0.35, 0.30, 0.15],
    "Prostate Cancer":   [0.40, 0.30, 0.20, 0.10],
    "Leukemia":          [0.15, 0.20, 0.40, 0.25],
    "Skin Cancer":       [0.45, 0.30, 0.15, 0.10],
    "Bladder Cancer":    [0.30, 0.35, 0.25, 0.10],
    "Kidney Cancer":     [0.25, 0.30, 0.30, 0.15],
    "Thyroid Cancer":    [0.55, 0.30, 0.10, 0.05],
    "Lymphoma":          [0.20, 0.30, 0.30, 0.20],
    "Pancreatic Cancer": [0.05, 0.10, 0.30, 0.55],
    "Cervical Cancer":   [0.30, 0.35, 0.25, 0.10],
}

stages = ["Stage I", "Stage II", "Stage III", "Stage IV"]

def get_age_range(age):
    if age < 13:
        return "Child"
    elif age < 18:
        return "Teenager"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"

def get_gender(cancer_type):
    if cancer_type == "Prostate Cancer":
        return "Male"
    elif cancer_type == "Cervical Cancer":
        return "Female"
    elif cancer_type == "Breast Cancer":
        return random.choices(["Female", "Male"], weights=[0.99, 0.01])[0]
    else:
        return random.choices(["Male", "Female"], weights=[0.50, 0.50])[0]

def get_age(cancer_type):
    if cancer_type == "Leukemia":
        return random.choices(
            [random.randint(5, 19), random.randint(40, 85)],
            weights=[0.3, 0.7]
        )[0]
    elif cancer_type == "Thyroid Cancer":
        return min(max(int(random.gauss(45, 15)), 18), 85)
    elif cancer_type in ["Pancreatic Cancer", "Prostate Cancer"]:
        return min(max(int(random.gauss(67, 10)), 40), 90)
    else:
        return min(max(int(random.gauss(58, 14)), 18), 90)

records = []
for i in range(1, N + 1):
    cancer_type = random.choices(cancer_types, weights=cancer_weights)[0]
    age         = get_age(cancer_type)
    gender      = get_gender(cancer_type)
    stage       = random.choices(stages, weights=stage_weights_map[cancer_type])[0]

    records.append({
        "patient_id":        f"PT-{i:04d}",
        "patient_age":       age,
        "age_range":         get_age_range(age),
        "gender":            gender,
        "cancer_types":      cancer_type,
        "cancer_stage_type": stage,
    })

df = pd.DataFrame(records)
df.to_csv("hospital_cancer_patients.csv", index=False)

print(f"CSV saved: hospital_cancer_patients.csv")
print(f"Total patients : {len(df)}")
print(f"\nAge Range:\n{df['age_range'].value_counts()}")
print(f"\nCancer Types:\n{df['cancer_types'].value_counts()}")
print(f"\nStage:\n{df['cancer_stage_type'].value_counts()}")
print(f"\nGender:\n{df['gender'].value_counts()}")
