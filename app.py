import streamlit as st
import joblib

# Load model & vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("spam_vectorizer.pkl")

st.title("📩 SpamShield AI – SMS Spam Classifier")
st.write("Enter a message to check whether it's spam or not.")


text = st.text_area("Message:", height=120)

if st.button("Analyze"):
    if text.strip() == "":
        st.warning("Please enter a message.")
    else:
        # Vectorize input text
        vec = vectorizer.transform([text])
        
        # Predict
        pred = model.predict(vec)[0]
        prob = model.predict_proba(vec)[0]

        if pred == 1:
            st.error(f"🚫 Spam Detected! (Confidence: {prob[1]*100:.2f}%)")
        else:
            st.success(f"✔️ Not Spam (Confidence: {prob[0]*100:.2f}%)")
