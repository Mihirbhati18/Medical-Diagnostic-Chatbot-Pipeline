# Medical Chatbot

An advanced, AI-powered medical chatbot designed to predict potential diseases based on user symptoms and analyze uploaded lab reports using Computer Vision and NLP.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation and Setup](#installation-and-setup)
- [Running the Project](#running-the-project)
- [Usage](#usage)

## Features
- **Symptom Checker**: Enter conversational text describing your symptoms, and the bot's Natural Language Processing model will identify them.
- **Disease Prediction**: Based on the collected symptoms, a Machine Learning model predicts the most likely disease and suggests precautions.
- **Lab Report Analyzer**: Upload a photo of a blood test/lab report. The system uses OCR (Optical Character Recognition) to extract values, flags abnormalities (High/Low), and automatically adds these as symptoms for prediction.

## Prerequisites
- **Python 3.10** installed on your system.
- **Tesseract OCR**: You must have Tesseract OCR installed on your Windows machine for the lab report analyzer to function.
  - Download and install from [UB-Mannheim Tesseract installer](https://github.com/UB-Mannheim/tesseract/wiki).
  - Ensure it installs to the default path (`C:\Program Files\Tesseract-OCR\tesseract.exe`).

## Installation and Setup

1. **Clone the repository** (or download the folder):
   ```bash
   git clone <your-repository-url>
   cd MedicalChatbot
   ```

2. **Create a Virtual Environment**:
   It is highly recommended to use a virtual environment to manage dependencies and avoid version conflicts.
   ```bash
   # Create a virtual environment named 'venv'
   python -m venv venv

   # Activate the virtual environment
   # On Windows:
   .\venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   Install all required packages from `requirements.txt`. Note that specific older versions of `scikit-learn` and `numpy` are required to maintain compatibility with the pre-trained models.
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **NLTK Data Download**:
   If this is your first time running NLTK, you may need to download the tokenizers. This happens automatically, but if you encounter errors, run this in python:
   ```python
   import nltk
   nltk.download('punkt')
   ```

## Running the Project

1. Open your terminal or command prompt.
2. Navigate to the project directory (`MedicalChatbot`).
3. Ensure your virtual environment is activated (`.\venv\Scripts\activate`).
4. Run the Flask application:
   ```bash
   python app.py
   ```
5. Open your web browser and navigate to:
   **http://127.0.0.1:5000/**

## Usage

1. **Chatting**: Type your symptoms naturally (e.g., "I have a headache and a severe fever"). The bot will register these symptoms.
2. **Predicting**: Once you have entered all your symptoms, type **"done"**. The bot will analyze your symptoms, predict the disease, provide a description, and list precautions.
3. **Lab Reports**: Click the attachment/upload icon to upload an image of a lab report. The bot will scan it, extract numerical values, check them against normal medical reference ranges, and add any abnormal findings (like "Low Hemoglobin" translating to "fatigue") directly into your symptom list!
