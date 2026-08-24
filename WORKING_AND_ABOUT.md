# Technical Architecture and Working

This document provides a deep dive into the technical aspects of the **Medical Chatbot**, explaining its underlying architecture, the technologies it uses, and exactly how the different components interact.

## 1. What the Project Is
The Medical Chatbot is a web-based artificial intelligence assistant tailored for basic medical triage. It serves two primary functions:
1. **Conversational Symptom Extraction**: It chats with users, understands their natural language inputs, and extracts specific medical symptoms.
2. **Lab Report Analysis**: It accepts uploaded images of physical lab reports (like blood tests), reads the text, and evaluates the medical markers.

It ultimately funnels all this information into a Machine Learning classifier to predict the most probable disease and advise the user on precautions.

---

## 2. Technical Architecture & Tech Stack

The system is built on a modular architecture using the following core technologies:

### **Backend (Web Framework)**
- **Flask (Python)**: Serves as the web server, handles API endpoints (`/symptom`, `/upload-lab-report`), and renders the frontend HTML templates. 

### **Natural Language Processing (NLP)**
- **NLTK (Natural Language Toolkit)**: Used for tokenization (breaking sentences into words) and stemming (reducing words to their root form).
- **PyTorch**: Powers a Feed-Forward Neural Network (`nnet.py`). This network is trained on `intents.json` to classify user inputs into specific symptom "tags" (e.g., mapping "my head hurts" to the "headache" symptom).

### **Computer Vision & OCR (Lab Analyzer)**
- **OpenCV (`cv2`)**: Pre-processes uploaded lab report images (grayscale conversion, denoising, adaptive thresholding) to make them readable.
- **Tesseract OCR (via `pytesseract`)**: An Optical Character Recognition engine that extracts raw text from the pre-processed images.

### **Machine Learning (Disease Prediction)**
- **Scikit-Learn**: Uses a pre-trained classification model (`models/fitted_model.pickle2`)—likely a Decision Tree or Random Forest based on the implementation—to predict a specific disease from a binary array of 132 possible symptoms.
- **Pandas & Numpy**: Used for data manipulation, formatting the input arrays for the ML model, and reading the CSV files containing disease descriptions, precautions, and severity weights.

### **Frontend**
- **HTML/CSS/Vanilla JavaScript**: A responsive, chat-like interface that communicates asynchronously with the Flask backend via AJAX/Fetch API.

---

## 3. How It Works (Step-by-Step Flow)

### A. The Conversational Flow
1. **User Input**: The user types a message in the chat UI.
2. **NLP Classification**: The message is sent to `/symptom`. The PyTorch neural network tokenizes the text, creates a "bag of words," and predicts the intent.
3. **Symptom Registration**: If the neural network is confident (>50%), the identified symptom is added to a temporary session set (`user_symptoms`).
4. **Disease Prediction (The "Done" Trigger)**: When the user types "done", the backend checks the `user_symptoms` set against the master list of all known symptoms, creating a binary array (e.g., `[0, 1, 0, 0, 1...]`).
5. **Output**: This array is fed into the Scikit-learn model, which outputs the predicted disease. The backend fetches the disease description and precautions from CSV files and returns them to the user. It also calculates a "severity score" to advise if a real doctor is urgently needed.

### B. The Lab Report Pipeline
When a user uploads an image of a lab report, the `lab_analyzer.py` module executes a 4-step pipeline:

1. **Vision (Image to Text)**: 
   OpenCV cleans the image (resizing, denoising, thresholding) to improve contrast. Tesseract OCR then scans the image and returns a giant string of raw text.
2. **Parse (Regex Extraction)**: 
   Regular expressions scan the raw text for specific markers (e.g., Hemoglobin, WBC, Glucose). It accounts for common aliases and extracts the numerical value next to them.
3. **Evaluate (Threshold Checking)**: 
   The extracted numbers are compared against hardcoded, standard medical reference ranges (e.g., Glucose should be between 70-110 mg/dL). If a value is outside the range, it is flagged as "High" or "Low".
4. **Integrate (Symptom Mapping)**: 
   The flagged abnormalities are mapped to physical symptoms based on medical correlations (e.g., Low Hemoglobin translates to "fatigue" and "breathlessness"). These derived symptoms are automatically injected into the user's `user_symptoms` set, enhancing the final disease prediction.

## 4. Specific Technical Requirements / Constraints
- **Model Versioning**: The Scikit-learn model was serialized (pickled) using `scikit-learn==1.2.2`. Unpickling it with newer versions (1.3+) causes `ValueError` crashes due to changes in how Decision Trees are structurally stored in memory. Therefore, strict versioning is enforced.
- **Numpy Binary Compatibility**: `scikit-learn 1.2.x` relies on C-extensions compiled against Numpy 1.x. Using Numpy 2.0+ results in a binary incompatibility (`numpy.dtype size changed`). Therefore, `numpy<2.0.0` is strictly required.
