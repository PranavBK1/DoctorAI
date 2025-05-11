import streamlit as st
from load_model import ask_ai

st.title("🧬 Doctor AI Assistant (BioGPT Version)")
st.write("Describe your symptoms to receive a possible medical insight.")

symptoms = st.text_area("Enter your symptoms here")

if st.button("Analyze"):
    if symptoms.strip():
        with st.spinner("Thinking..."):
            response = ask_ai(symptoms)
        st.success("Here's what BioGPT thinks:")
        st.write(response)
    else:
        st.error("Please enter some symptoms.")

