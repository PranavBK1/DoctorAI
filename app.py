import streamlit as st
from load_model import ask_ai

st.set_page_config(page_title="AI Medical Symptom Checker", page_icon="🩺")

st.title("🩺 AI Medical Symptom Checker")
st.write("Describe your symptoms below and get a likely medical condition in response.")

symptoms = st.text_area("Describe your symptoms here:", height=150)

if st.button("Get Diagnosis"):
    if symptoms.strip():
        with st.spinner("Analyzing your symptoms..."):
            diagnosis = ask_ai(symptoms)
        st.success("Likely Condition:")
        st.write(diagnosis)
    else:
        st.error("Please enter your symptoms before submitting.")
