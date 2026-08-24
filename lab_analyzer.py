"""
Lab Report Analyzer — 4-Step OCR Pipeline
==========================================
Step 1 (Vision):    OpenCV + Tesseract OCR  →  raw text
Step 2 (Parse):     Regex extraction        →  structured lab values
Step 3 (Evaluate):  Medical thresholds      →  High / Low / Normal flags
Step 4 (Integrate): Symptom mapping         →  ML-ready symptom set
"""

import re
import os
import cv2
import numpy as np
import pytesseract
from PIL import Image

# ---------------------------------------------------------------------------
# Configure Tesseract path (Windows default install location)
# ---------------------------------------------------------------------------
_TESSERACT_PATHS = [
    r"C:\Program Files\Tesseract-OCR\tesseract.exe",
    r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
]
for _p in _TESSERACT_PATHS:
    if os.path.isfile(_p):
        pytesseract.pytesseract.tesseract_cmd = _p
        break

# ============================================================================
# STEP 1 — VISION: Read the image and extract raw text
# ============================================================================

def preprocess_image(image_path: str) -> np.ndarray:
    """Apply OpenCV preprocessing for better OCR accuracy."""
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Cannot read image: {image_path}")

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Resize if image is small (helps Tesseract)
    h, w = gray.shape
    if w < 1000:
        scale = 1000 / w
        gray = cv2.resize(gray, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)

    # Denoise
    gray = cv2.fastNlMeansDenoising(gray, h=15)

    # Adaptive thresholding for varied lighting
    processed = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 10
    )

    return processed


def extract_text_from_image(image_path: str) -> str:
    """Step 1: Use OpenCV + Tesseract to convert an image to raw text."""
    processed = preprocess_image(image_path)

    # Tesseract config: treat as a single block of text, whitelist useful chars
    custom_config = r"--oem 3 --psm 6"
    raw_text = pytesseract.image_to_string(processed, config=custom_config)

    return raw_text


# ============================================================================
# STEP 2 — PARSE: Extract specific lab marker values via regex
# ============================================================================

# Each entry: (display_name, [regex_aliases], unit)
LAB_MARKERS = [
    ("Hemoglobin",       [r"h(?:ae)?moglobin", r"\bhb\b", r"\bhgb\b"],                    "g/dL"),
    ("WBC",              [r"wbc", r"white\s*blood\s*cell", r"leucocyte", r"leukocyte"],    "cells/µL"),
    ("RBC",              [r"rbc", r"red\s*blood\s*cell", r"erythrocyte"],                  "million/µL"),
    ("Platelet",         [r"platelet", r"\bplt\b"],                                        "cells/µL"),
    ("Glucose",          [r"glucose", r"\bfbs\b", r"fasting\s*blood\s*sugar"],             "mg/dL"),
    ("Cholesterol",      [r"cholesterol", r"total\s*cholesterol"],                          "mg/dL"),
    ("Creatinine",       [r"creatinine"],                                                   "mg/dL"),
    ("Bilirubin",        [r"bilirubin"],                                                    "mg/dL"),
    ("ALT",              [r"\balt\b", r"sgpt"],                                             "U/L"),
    ("AST",              [r"\bast\b", r"sgot"],                                             "U/L"),
    ("TSH",              [r"\btsh\b", r"thyroid\s*stimulating"],                            "mIU/L"),
    ("Uric Acid",        [r"uric\s*acid"],                                                  "mg/dL"),
]


def parse_lab_values(raw_text: str) -> list[dict]:
    """
    Step 2: Hunt through OCR text and extract numerical values for each marker.
    Returns a list of dicts: {name, value, unit}
    """
    results = []
    text_lower = raw_text.lower()

    for display_name, aliases, unit in LAB_MARKERS:
        for alias in aliases:
            # Pattern: marker name ... optional colon/spaces ... number (with optional decimal)
            pattern = alias + r"[\s:;\-\|]*(\d+\.?\d*)"
            match = re.search(pattern, text_lower)
            if match:
                value = float(match.group(1))
                results.append({
                    "name":  display_name,
                    "value": value,
                    "unit":  unit,
                })
                break  # found this marker, move to next

    return results


# ============================================================================
# STEP 3 — EVALUATE: Check values against standard medical thresholds
# ============================================================================

# Reference ranges (adult, general — conservative)
# Format: (low_bound, high_bound)  — values outside this range are flagged
REFERENCE_RANGES = {
    "Hemoglobin":   (12.0, 17.5),    # g/dL
    "WBC":          (4000, 11000),    # cells/µL
    "RBC":          (4.0, 5.9),       # million/µL
    "Platelet":     (150000, 400000), # cells/µL
    "Glucose":      (70, 110),        # mg/dL (fasting)
    "Cholesterol":  (0, 200),         # mg/dL (total)
    "Creatinine":   (0.6, 1.2),       # mg/dL
    "Bilirubin":    (0.1, 1.2),       # mg/dL (total)
    "ALT":          (7, 56),          # U/L
    "AST":          (10, 40),         # U/L
    "TSH":          (0.4, 4.0),       # mIU/L
    "Uric Acid":    (3.5, 7.2),       # mg/dL
}


def evaluate_lab_values(parsed_values: list[dict]) -> list[dict]:
    """
    Step 3: Compare each extracted value to its reference range.
    Adds 'status' ("High", "Low", "Normal") and 'ref_range' to each dict.
    """
    evaluated = []
    for entry in parsed_values:
        name  = entry["name"]
        value = entry["value"]
        ref   = REFERENCE_RANGES.get(name)

        if ref is None:
            status = "Unknown"
            ref_str = "N/A"
        else:
            low, high = ref
            if value < low:
                status = "Low"
            elif value > high:
                status = "High"
            else:
                status = "Normal"
            ref_str = f"{low}–{high}"

        evaluated.append({
            **entry,
            "status":    status,
            "ref_range": ref_str,
        })

    return evaluated


# ============================================================================
# STEP 4 — ML INTEGRATION: Map abnormal findings → model symptoms
# ============================================================================

# CONSERVATIVE mapping: only the 1–2 most tightly correlated symptoms per finding
# Every symptom listed here exists in the model's list_of_symptoms.pickle
SYMPTOM_MAP = {
    ("Hemoglobin",  "Low"):   ["fatigue", "breathlessness"],
    ("Hemoglobin",  "High"):  [],  # usually benign, no mapping

    ("WBC",         "High"):  ["high_fever"],
    ("WBC",         "Low"):   ["fatigue"],

    ("RBC",         "Low"):   ["fatigue", "breathlessness"],
    ("RBC",         "High"):  [],

    ("Platelet",    "Low"):   ["bruising"],
    ("Platelet",    "High"):  [],

    ("Glucose",     "High"):  ["excessive_hunger", "polyuria"],
    ("Glucose",     "Low"):   ["sweating", "dizziness"],

    ("Cholesterol", "High"):  ["chest_pain"],

    ("Creatinine",  "High"):  ["swelling_joints", "dark_urine"],

    ("Bilirubin",   "High"):  ["yellowish_skin", "yellowing_of_eyes"],

    ("ALT",         "High"):  ["abdominal_pain", "yellowish_skin"],

    ("AST",         "High"):  ["abdominal_pain", "nausea"],

    ("TSH",         "High"):  ["weight_gain", "fatigue"],
    ("TSH",         "Low"):   ["weight_loss", "fast_heart_rate"],

    ("Uric Acid",   "High"):  ["joint_pain"],
}


def map_to_symptoms(evaluated_values: list[dict]) -> set[str]:
    """
    Step 4: Translate flagged lab findings into ML-model symptoms.
    Returns a set of symptom strings ready to merge with user_symptoms.
    """
    derived_symptoms = set()

    for entry in evaluated_values:
        key = (entry["name"], entry["status"])
        symptoms = SYMPTOM_MAP.get(key, [])
        derived_symptoms.update(symptoms)

    return derived_symptoms


# ============================================================================
# FULL PIPELINE — Convenience function
# ============================================================================

def analyze_lab_report(image_path: str) -> dict:
    """
    Run the complete 4-step pipeline on a lab report image.

    Returns:
        {
            "raw_text":       str,
            "parsed_values":  [...],
            "evaluated":      [...],
            "derived_symptoms": set[str],
            "success":        bool,
            "error":          str | None,
        }
    """
    try:
        raw_text        = extract_text_from_image(image_path)
        parsed_values   = parse_lab_values(raw_text)

        if not parsed_values:
            return {
                "raw_text":          raw_text,
                "parsed_values":     [],
                "evaluated":         [],
                "derived_symptoms":  set(),
                "success":           False,
                "error":             "Could not detect any lab markers in the image. Please upload a clearer photo of your lab report.",
            }

        evaluated        = evaluate_lab_values(parsed_values)
        derived_symptoms = map_to_symptoms(evaluated)

        return {
            "raw_text":          raw_text,
            "parsed_values":     parsed_values,
            "evaluated":         evaluated,
            "derived_symptoms":  derived_symptoms,
            "success":           True,
            "error":             None,
        }

    except FileNotFoundError as e:
        return {
            "raw_text": "", "parsed_values": [], "evaluated": [],
            "derived_symptoms": set(), "success": False, "error": str(e),
        }
    except Exception as e:
        return {
            "raw_text": "", "parsed_values": [], "evaluated": [],
            "derived_symptoms": set(), "success": False,
            "error": f"Processing error: {str(e)}",
        }
