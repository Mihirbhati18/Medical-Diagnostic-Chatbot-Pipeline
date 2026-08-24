import os
from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (1000, 1100), color='white')
d = ImageDraw.Draw(img)

# Try to use standard Windows fonts to make the report look realistic
try:
    font_title = ImageFont.truetype("arialbd.ttf", 36)
    font_header = ImageFont.truetype("arial.ttf", 22)
    font_body = ImageFont.truetype("cour.ttf", 24)
except IOError:
    font_title = font_header = font_body = ImageFont.load_default()

# ─── HEADER ───
d.text((50, 50), "GLOBAL DIAGNOSTICS LABORATORY", fill=(0, 0, 0), font=font_title)
d.text((50, 100), "123 Health Way, Metropolis | Phone: 555-0199", fill=(100, 100, 100), font=font_header)
d.line([(50, 140), (950, 140)], fill=(0, 0, 0), width=3)

# ─── PATIENT INFO ───
d.text((50, 160), "Patient Name: Jane Doe", fill=(0, 0, 0), font=font_header)
d.text((50, 190), "Patient ID:   MRN-847291", fill=(0, 0, 0), font=font_header)
d.text((600, 160), "Collected: 11-Apr-2026", fill=(0, 0, 0), font=font_header)
d.text((600, 190), "Reported:  12-Apr-2026", fill=(0, 0, 0), font=font_header)
d.line([(50, 230), (950, 230)], fill=(0, 0, 0), width=1)

# ─── REPORT TITLE ───
d.text((50, 260), "COMPREHENSIVE METABOLIC & CBC PANEL", fill=(0, 0, 0), font=font_title)

# ─── TABLE HEADER ───
d.text((50, 330), "TEST", fill=(0, 0, 0), font=font_header)
d.text((350, 330), "RESULT", fill=(0, 0, 0), font=font_header)
d.text((500, 330), "FLAG", fill=(0, 0, 0), font=font_header)
d.text((650, 330), "UNITS", fill=(0, 0, 0), font=font_header)
d.text((800, 330), "REFERENCE", fill=(0, 0, 0), font=font_header)
d.line([(50, 360), (950, 360)], fill=(0, 0, 0), width=2)

# ─── TABLE ROW DATA ───
# Mixing normal results with abnormal ones so the Chatbot can demonstrate its extraction and diagnosis capabilities.
lines = [
    ("Hemoglobin",      "14.5",  "",     "g/dL",       "12.0 - 17.5"),
    ("WBC",             "8500",  "",     "cells/uL",   "4000 - 11000"),
    ("RBC",             "5.0",   "",     "million/uL", "4.0 - 5.9"),
    ("Platelet",        "250000","",     "cells/uL",   "150k - 400k"),
    ("Glucose",         "145",   "HIGH", "mg/dL",      "70 - 110"),   # High Glucose
    ("Cholesterol",     "230",   "HIGH", "mg/dL",      "< 200"),      # High Cholesterol
    ("Creatinine",      "0.9",   "",     "mg/dL",      "0.6 - 1.2"),
    ("Bilirubin",       "2.1",   "HIGH", "mg/dL",      "0.1 - 1.2"),  # High Bilirubin
    ("ALT",             "65",    "HIGH", "U/L",        "7 - 56"),     # High ALT
    ("AST",             "20",    "",     "U/L",        "10 - 40"),
    ("TSH",             "2.4",   "",     "mIU/L",      "0.4 - 4.0"),
    ("Uric Acid",       "5.2",   "",     "mg/dL",      "3.5 - 7.2"),
]

y = 400
for test, res, flag, unit, ref in lines:
    color = (200, 0, 0) if flag else (0, 0, 0)
    d.text((50, y), test, fill=(0, 0, 0), font=font_body)
    d.text((350, y), res, fill=color, font=font_body)
    d.text((500, y), flag, fill=color, font=font_body)
    d.text((650, y), unit, fill=(0, 0, 0), font=font_body)
    d.text((800, y), ref, fill=(0, 0, 0), font=font_body)
    y += 45

# ─── FOOTER ───
d.line([(50, y + 20), (950, y + 20)], fill=(0, 0, 0), width=1)
d.text((50, y + 40), "*** End of Report ***", fill=(0, 0, 0), font=font_header)
d.text((50, y + 80), "Please consult your physician for clinical interpretation.", fill=(100, 100, 100), font=font_header)

output_path = os.path.join(os.path.dirname(__file__), 'sample_lab_report.png')
img.save(output_path)
print(f"Generated realistic dummy report at {output_path}")
