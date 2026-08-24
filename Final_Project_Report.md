Medical Chatbot with OCR-Based Lab Report Integration
Machine Learning & Data Science Project Report
________________________________________

Abstract 
This project presents a full-stack AI-powered Medical Chatbot that integrates Natural Language Processing (NLP), Machine Learning (ML), and Optical Character Recognition (OCR) to assist in disease prediction. Unlike traditional systems that rely only on user-entered symptoms, this chatbot can also process lab report images and extract clinical data.
The system uses OpenCV and Tesseract OCR to extract medical values, which are evaluated and mapped to symptoms. These symptoms are combined with user input and fed into a Scikit-Learn model for disease prediction. A PyTorch-based NLP model is used to understand user text.
This hybrid system improves diagnostic accuracy and demonstrates the effective integration of computer vision and machine learning in healthcare.
________________________________________

1. Introduction
This project presents an intelligent medical chatbot capable of predicting diseases based on user symptoms. The system has been enhanced with an OCR-based lab report analysis feature, allowing it to process physical blood test reports and integrate clinical data into its prediction pipeline.
________________________________________

2. Problem Statement 
Traditional chatbot systems rely only on user-input symptoms, which can be incomplete or inaccurate. They do not utilize real clinical data such as lab reports.
This project aims to solve this problem by:
Integrating lab report analysis with symptom-based machine learning models to improve diagnostic accuracy.
________________________________________

3. Objectives
• To build an intelligent chatbot capable of predicting diseases 
• To integrate image-based lab report analysis 
• To combine user-entered symptoms with lab-derived data 
• To improve prediction accuracy using multiple inputs 
________________________________________

4. System Architecture
4.1 High-Level Flow
User Input (Text) → NLP Model → Symptoms
                         ↓
Lab Report Image → OCR → Extracted Values → Evaluation → Symptoms
                         ↓
                Combined Symptoms → ML Model → Disease Prediction
________________________________________

5. Technologies Used
Programming & Frameworks:
• Python, Flask 
Machine Learning:
• PyTorch, Scikit-Learn 
NLP:
• NLTK 
Computer Vision:
• OpenCV, pytesseract, Tesseract OCR 
Frontend:
• HTML, CSS, JavaScript 
________________________________________

6. Machine Learning Models & Training Details

> **Model Training & Dataset Information**
> - **Primary Dataset (`dataset.csv`)**: The prediction model was trained on a comprehensive healthcare dataset containing **4,920 records**, mapping patients' varied symptoms to specific underlying diseases.
> - **Symptom Vectorization**: Inputs are transformed using hot-encoded symptom arrays mapped against a generated `list_of_symptoms.pickle`.
> - **Data Scaling**: Weighted penalty thresholds are utilized during execution. Symptoms are checked against `Symptom-severity.csv`, evaluating both maximum and mean severity. If symptoms pass critical severity threshold metrics, the system automatically injects a medical warning.

6.1 NLP Model (PyTorch)
• Architecture: Feedforward Neural Network.
• Configuration: 3 Linear layers + ReLU activation. The network uses `Cross Entropy Loss` for its classification, optimizing out the need for an explicit final soft-max activation layer in the architecture.
• Input Format: Bag-of-Words input arrays mapped over vocabulary tensors.
• Output: Generates direct symptom classifications using intent mapping.

6.2 Disease Prediction Model (Scikit-Learn)
• Algorithm: Random Forest Classifier (saved via protocol as `fitted_model.pickle2`).
• Input: Uses generalized symptom vectors merged from NLP chatbot intent blocks and visual OCR derived values.
• Output: Predicts the final underlying disease based on the 4920×132 training matrix structure.
________________________________________

7. OCR Lab Report Integration
Overview:
Step 1: Vision (Advanced Preprocessing Operations)
• Grayscale conversion.
• Utilized OpenCV's `fastNlMeansDenoising` algorithm and `adaptiveThreshold` (Gaussian) to mitigate varied lighting conditions, camera shadows, and picture noise. This drastically improves resulting string extractions.
• Text extraction via Tesseract OCR framework bounding parameters.

Step 2: Parsing (Regular Expression Logic)
• Extracts 12 specific medical markers: Hemoglobin, WBC, RBC, Platelets, Glucose, Cholesterol, Creatinine, Bilirubin, ALT, AST, TSH, Uric Acid.
• Implemented a robust Regular Expression (Regex) matching engine with alias mapping. This enables the model to accurately identify numerical markers despite wild laboratory naming discrepancies and abbreviations (e.g., classifying "FBS", "fbs", and "fasting blood sugar" uniformly as Glucose).

Step 3: Evaluation
• Compares extracted values against structured conservative medical reference boundaries.
• Classifies numeric states dynamically into evaluated categories: Normal, High, Low.

Step 4: ML Integration (Conservative Mapping)
• Extrapolates abnormal string-state values back to equivalent vectors capable of ingestion by the ML prediction model.
• Example Mappings: 
  o Low Platelets → bruising 
  o High Glucose → excessive_hunger, polyuria
  o Low TSH → weight loss
________________________________________

8. Backend Implementation
• Flask-based backend framework.
• Symptom Severity Warning System: Calculates array maximums and weighted means on active symptoms. Safely recommends immediate direct medical attention if danger thresholds are met.
• Endpoints implemented: `POST /upload-lab-report`, `POST /symptom`, `GET /`
• Upload pipeline optimally handles multipart-form image streams, initiates the 4-step OCR processing pipeline seamlessly, and joins derived symptoms autonomously back to the user-state.
________________________________________

9. Frontend Implementation
• Responsive DOM manipulation layout rendering without required browser refreshes via active state injection.
• Features: Context-aware scanning animations, dynamic diagnosis result outputs structured in custom card layouts.
• UI Design Architecture: Created via dynamic modern web engineering including premium Glass-morphism elements and CSS-rendered dynamic condition coloring: 
  o 🟩 Green for Normal references. 
  o 🟥 Red for High references. 
  o 🟦 Blue for Low references. 
________________________________________

10. Data Handling Sub-Components
• `dataset.csv`: Primary machine-learning training data-matrix (4,920 record iterations).
• `Symptom-severity.csv`: Medical risk symptom danger parameters.
• `symptom_Description.csv`: Output definition map.
• `symptom_precaution.csv`: Prescriptive secondary conditions matched to initial results.
• `list_of_symptoms.pickle`: Read-only optimized serialized vector array framework cache.
________________________________________

11. Results 
The completed system successfully:
• Parses and extracts functional numerical lab values from unstructured images overriding varying quality types.
• Uses statistical rigid bounds for categorization logic evaluations.
• Maps conservative clinical findings to established NLP-trained model symptoms successfully.
• Calculates comprehensive ML matrix algorithms utilizing combinations of both textual input and image-analysis vectors concurrently.
• Generates and outputs accurate predictive clinical diagnosis findings dynamically based on integrated source matrices.
________________________________________

12. Testing & Validation
Manual Testing
• Evaluated via various real-world sample proprietary lab report images.
• Audited standard character recognition accuracy bounds directly against baseline control-copies.
Planned Automated Testing
• Build distinct Unit Testing assertions checking Regex array data blocks.
• Integrate tests validating conditional logic boundary triggers correctly scale.
• Complete end-to-end multi-state payload API integration assessments via CI hooks.
________________________________________

13. Advantages
• Genuine hybrid diagnostic AI model supporting robust textual intent mapping merged with visual quantitative input parameters.
• Effectively avoids the single-point constraint limit found in conventional AI bots through authentic verified physical evidence points mapping.
• Highly performant real-time analysis optimized utilizing specialized PyTorch model evaluation triggers (`.eval()`) and serialized Scikit-learn deployment states.
• Professional design implementation backed by automated clinical severity guardrails.
________________________________________

14. Limitations
• Total character detection accuracy rates remain primarily linked to camera focal alignment qualities and external source illumination boundaries.
• Lack of immediate pre-built CI/CD automation test coverage workflows.
• Targeted image analysis is intentionally scoped to a restrictive 12 high-priority medical categories requiring active expansion updates.
________________________________________

15. Future Scope 
• Upgrade logic CV extractions by removing standard Tesseract frameworks, substituting deep learning-based spatial array replacements (e.g. YOLO/LayoutLM + EasyOCR combinations).
• Build support covering multi-lingual global tokenization models natively.
• Finalize scalable AWS/GCP cloud application deployment parameters handling independent micro-service data flow layers.
• Engineer custom mapping logic API gateways compliant with FHIR/HL7 database patient records integrations inside actual clinical hospitals.
________________________________________

16. Conclusion
This deployment cleanly integrates intricate Natural Language Processing rulesets, serialized Machine Learning arrays, and programmatic Computer Vision image processing pipelines to form a responsive AI healthcare architecture. Applying dynamically parsed document logic into primary predictive calculations definitively bridges previous gaps within digital triage bot limits, reinforcing the robust future potential behind functional AI workflow applications executed directly inside the medical domain.
