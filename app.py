import streamlit as st
import joblib

st.title("📨 SpamShield AI")
st.subheader("Detect whether an SMS message is Spam or Not Spam")

model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("spam_model.pkl")

text = st.text_area("Enter SMS text:", height=150)

if st.button("Analyze"):
    vec = vectorizer.transform([text])
    pred = model.predict(vec)[0]
    if pred == 1:
        st.error("🚫 Spam Detected")
    else:
        st.success("✅ Safe Message")
