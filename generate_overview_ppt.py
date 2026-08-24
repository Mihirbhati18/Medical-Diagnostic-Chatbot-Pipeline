import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN

def create_full_overview_ppt():
    prs = Presentation()
    
    # helper for adding a standard bullet slide
    def add_bullet_slide(prs, title_text, bullets):
        slide_layout = prs.slide_layouts[1] # Title and Content
        slide = prs.slides.add_slide(slide_layout)
        title = slide.shapes.title
        title.text = title_text
        content_box = slide.placeholders[1]
        tf = content_box.text_frame
        tf.clear()
        for i, point in enumerate(bullets):
            p = tf.add_paragraph()
            p.text = point
            p.level = 0
            # A little formatting to space lines out slightly
            p.space_before = Pt(12)
        return slide

    # --- Slide 1: Title ---
    slide_layout = prs.slide_layouts[0] # Title Slide
    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    subtitle = slide.placeholders[1]
    title.text = "Medical Chatbot with OCR-Based Lab Report Integration"
    subtitle.text = "Machine Learning & Data Science Project Overview\nAn End-to-End AI Diagnostic System"

    # --- Slide 2: Abstract & Problem Statement ---
    add_bullet_slide(prs, "Problem Statement & Abstract", [
        "Current medical chatbots rely solely on user-entered symptoms, leading to misdiagnoses or incomplete data.",
        "Clinical data (lab reports) is highly valuable but strictly separated from standard AI triage bots.",
        "Solution: A hybrid AI system that processes both raw user text (NLP) AND physical blood test lab reports (OCR).",
        "Improves diagnostic accuracy significantly by combining qualitative feelings with quantitative clinical evidence."
    ])

    # --- Slide 3: Project Objectives ---
    add_bullet_slide(prs, "Project Objectives", [
        "1. Build an intelligent NLP conversational agent capable of understanding contextual textual symptoms.",
        "2. Integrate advanced Computer Vision (CV) to extract medical values from physical report images.",
        "3. Evaluate structured numerical boundary states (Normal, High, Low) directly from extracted text.",
        "4. Combine user text symptoms + extracted lab warnings into a single high-accuracy diagnostic ML model."
    ])

    # --- Slide 4: System Architecture ---
    slide_layout = prs.slide_layouts[1]
    slide = prs.slides.add_slide(slide_layout)
    slide.shapes.title.text = "System Architecture Model Flow"
    tf = slide.placeholders[1].text_frame
    tf.text = "Our Dual-Input Pipeline processing framework:"
    p = tf.add_paragraph()
    p.text = "USER INPUT (TEXT)  ──>  NLP Model (PyTorch)  ──> EXTRACTED SYMPTOMS"
    p.level = 1; p.space_before = Pt(14)
    p = tf.add_paragraph()
    p.text = "LAB REPORT (IMAGE) ──>  OCR Pipeline (Tesseract) ──> EVALUATED SYMPTOMS"
    p.level = 1; p.space_before = Pt(14)
    p = tf.add_paragraph()
    p.text = "COMBINED SYMPTOMS  ──>  ML Model (Scikit-Learn)  ──> DISEASE PREDICTION"
    p.level = 0; p.space_before = Pt(24)

    # --- Slide 5: Technologies Used ---
    add_bullet_slide(prs, "Technology Stack", [
        "• Core Framework: Python & Flask (Backend Web Server API)",
        "• Deep Learning NLP: PyTorch & NLTK (Text Intent Mapping)",
        "• Machine Learning: Scikit-Learn / Random Forest (Matrix Classification)",
        "• Computer Vision: OpenCV & Tesseract OCR (Image processing & layout parsing)",
        "• Frontend UI: HTML5, CSS3, Vanilla JS (Responsive, Client-side DOM manipulation)"
    ])

    # --- Slide 6: The Machine Learning Models ---
    add_bullet_slide(prs, "Machine Learning & NLP Pipelines", [
        "Data Source: Trained on a comprehensive 4,920 record healthcare dataset spanning 132 different symptom vectors.",
        "NLP Model (PyTorch): A robust Feedforward Neural Network using Cross-Entropy loss mapping user input directly to symptom intents without soft-max layers.",
        "Classification Model (Scikit-Learn): An optimized Random Forest Classifier selected specifically to prevent over-fitting on high-dimensional boolean array structures."
    ])

    # --- Slide 7: OCR 4-Step Integration Pipeline ---
    add_bullet_slide(prs, "OCR Lab Report Processing Logic", [
        "Step 1 (Vision): OpenCV fastNlMeansDenoising & adaptiveThreshold algorithms stabilize camera quality and shadow interference.",
        "Step 2 (Parsing): Heavy Regex architectures filter 12 high-priority medical markers (e.g., Glucose, Cholesterol, RBC).",
        "Step 3 (Evaluation): Dynamically categorizes scraped numerics into conservative clinical bounds (Normal/High/Low).",
        "Step 4 (Mapping): Injects mapped equivalents directly back into the ML context array automatically (e.g., High Glucose → excessive_hunger)."
    ])

    # --- Slide 8: Backend & Frontend Mechanics ---
    add_bullet_slide(prs, "Application Interfaces", [
        "Backend (Flask):",
        "  - Calculates symptom array severity triggers (alerts user on dangerous conditions).",
        "  - Optimizes memory usage using PyTorch .eval() hooks and serialized Model weights.",
        "Frontend UI:",
        "  - Fluid CSS Glass-morphism layouts preventing browser refresh jarring.",
        "  - Dynamic condition coloring (Green = Normal, Red = High, Blue = Low) visualizing lab findings seamlessly to users."
    ])

    # --- Slide 9: Advantages & Limitations ---
    add_bullet_slide(prs, "Advantages & Known Limitations", [
        "Advantages:",
        "  - Authentic visual diagnostic parameters merge successfully with textual inputs.",
        "  - Fully integrated severity guard-rails dynamically warn patients of life-threatening metrics.",
        "Limitations:",
        "  - OCR extraction remains heavily tied to image illumination/focal geometry limits.",
        "  - Image tracking currently restricted to 12 primary category buckets."
    ])

    # --- Slide 10: Conclusion & Scope ---
    add_bullet_slide(prs, "Conclusion & Future Scope", [
        "Conclusion:",
        "  - Developed a scalable integration of NLP rulesets, ML arrays, and CV image processing pipelines to handle modern diagnostic digital triage cleanly.",
        "Future Developments:",
        "  - Phase out standard Tesseract logic with Deep Learning Spatial (YOLO + EasyOCR) layouts.",
        "  - Prepare codebase for GCP/AWS isolated micro-services application hosting.",
        "  - Construct APIs compliant with actual FHIR/HL7 hospital database protocols."
    ])

    # Save Presentation
    output_filename = "Medical_Chatbot_Full_Overview.pptx"
    prs.save(output_filename)
    return output_filename

if __name__ == '__main__':
    created_file = create_full_overview_ppt()
    print(f"Full Overview Presentation Successfully Created: {created_file}")
