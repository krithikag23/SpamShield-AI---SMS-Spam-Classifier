# 📩 SpamShield AI — SMS Spam Classifier

SpamShield AI is a machine-learning powered web application that classifies SMS text messages as **Spam** or **Not Spam (Ham)**.  
It includes a **full model training pipeline**, **saved model files**, and a **Streamlit web application** for real-time predictions.

This project uses a traditional NLP + ML pipeline (**CountVectorizer + Logistic Regression**) which is lightweight, extremely fast, and highly accurate for short text like SMS messages.

SpamShield AI works completely offline — no API calls, no external dependencies, no dataset downloads manually.

---

## 🚀 Project Overview

SpamShield AI aims to detect unwanted text messages using NLP.  
This project provides:

- A Google Colab notebook to train the model  
- Automatic saving of the trained model as `spam_model.pkl`  
- A saved vectorizer (`vectorizer.pkl`) for text preprocessing  
- A professional Streamlit web application for real-time classification  
- Clean confidence scores for transparency  
- Supports any type of SMS — promotional, fraud, normal messages, reminders  

The system uses supervised learning to distinguish harmful text from safe ones.

---

## ✨ Features

- ⚡ **Fast training**  
- 📊 **High accuracy (≈ 96–97%)**  
- 🧠 **Uses Logistic Regression (light + interpretable)**  
- 🔡 **Bag-of-Words text vectorization**  
- 🌐 **Streamlit-based web UI**  
- ✨ **Confidence score for prediction**  
- 🔒 Fully offline, secure  
- 📱 Designed specifically for SMS-style short messages  

---

## 📚 Dataset Used

Dataset: **SMS Spam Collection Dataset**  
Source: UCI Machine Learning Repository  
Format:  
- 5,574 SMS messages  
- Labels → `ham` or `spam`  

The dataset is automatically loaded using a direct URL in the Colab training script.

---

## 🧠 ML Model Details

Model pipeline:

| Step | Description |
|------|-------------|
| **Vectorization** | CountVectorizer (Bag-of-Words) |
| **Classifier** | Logistic Regression |
| **Split** | 80% training — 20% testing |
| **Metrics** | Accuracy, Precision, Recall, F1-score |

This classical ML pipeline is perfect for small-text classification.

---

## 🔍 Sample Input & Output

### **Sample Input (User enters in app):**
Congratulations! You've won a $1000 Walmart gift card. Click the link to claim

### **Sample Output:**
🚫 Spam Detected! (Confidence: 92.14%)
