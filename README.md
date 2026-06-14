# Hospital Cancer Patient Azure Databricks

A simulated hospital cancer patient dataset (600 patients) built with Python and Faker, designed for use with Azure Databricks.

## Dataset Fields
- `patient_id` — Unique patient identifier (PT-0001 to PT-0600)
- `patient_age` — Age of the patient
- `age_range` — Child, Teenager, Adult, Senior
- `gender` — Male / Female
- `cancer_types` — 12 cancer types (e.g. Breast Cancer, Lung Cancer)
- `cancer_stage_type` — Stage I, II, III, IV

## Files
- `hospital_cancer_patients.csv` — Simulated patient dataset
- `faker_cancer_dataset.py` — Script to regenerate the dataset

## Requirements
```bash
pip install faker pandas
```

## Usage
```bash
python faker_cancer_dataset.py
```

