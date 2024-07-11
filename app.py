from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.set_page_config(page_title="LLM Project")

st.header("LLM Gemini Application")

input = st.text_input("Ask something...", key='input')

submit = st.button("Submit")

def get_gemini_model_respone(question):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(question)
    return response.text

if submit:
    model_response = get_gemini_model_respone(input)
    st.write(model_response)