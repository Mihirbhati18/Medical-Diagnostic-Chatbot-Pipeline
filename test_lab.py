"""Quick test of the lab_analyzer pipeline with simulated text."""
from lab_analyzer import parse_lab_values, evaluate_lab_values, map_to_symptoms

# Simulate OCR output from a lab report with some abnormal values
sample_text = """
COMPLETE BLOOD COUNT REPORT
Patient Name: Test Patient

Hemoglobin: 9.2 g/dL
WBC: 15000 cells/uL
RBC: 3.8 million/uL
Platelet: 120000 cells/uL
Glucose: 250 mg/dL
Cholesterol: 180 mg/dL
Creatinine: 0.9 mg/dL
Bilirubin: 3.5 mg/dL
ALT: 78 U/L
AST: 35 U/L
TSH: 0.2 mIU/L
Uric Acid: 8.5 mg/dL
"""

print("=" * 60)
print("STEP 2 — PARSING")
print("=" * 60)
parsed = parse_lab_values(sample_text)
for p in parsed:
    print(f"  {p['name']:15s} = {p['value']} {p['unit']}")

print(f"\nFound {len(parsed)} markers\n")

print("=" * 60)
print("STEP 3 — EVALUATION")
print("=" * 60)
evaluated = evaluate_lab_values(parsed)
for e in evaluated:
    flag = "!!" if e["status"] != "Normal" else "OK"
    print(f"  {flag} {e['name']:15s} = {e['value']:>10} {e['unit']:15s} [{e['status']:6s}] ref: {e['ref_range']}")

print()

print("=" * 60)
print("STEP 4 — SYMPTOM MAPPING (Conservative)")
print("=" * 60)
symptoms = map_to_symptoms(evaluated)
print(f"  Derived symptoms: {symptoms}")
print(f"  Count: {len(symptoms)}")
