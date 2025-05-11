import streamlit as st
from load_model import ask_ai

st.set_page_config(page_title="Doctor AI Assistant", page_icon="🧬")
st.title("🧬 Doctor AI Assistant (Powered by BioGPT)")
st.write("Describe your symptoms, and get AI-generated medical insights.")

# Input box
symptoms = st.text_area("🩺 Enter your symptoms (e.g., fatigue, chest pain):")

# Button to trigger analysis
if st.button("Analyze Symptoms"):
    if symptoms.strip():
        with st.spinner("Analyzing... please wait."):
            try:
                response = ask_ai(symptoms)
                st.success("✅ AI Response:")
                st.write(response)
            except Exception as e:
                st.error("⚠️ Something went wrong.")
                st.exception(e)
    else:
        st.warning("Please enter some symptoms to analyze.")


