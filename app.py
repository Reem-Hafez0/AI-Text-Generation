import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai

#load environment variables

load_dotenv()

google_api= os.getenv("GOOGLE_API_KEY")

if google_api:
    genai.configure(api_key=google_api)
else:
    st.error("Google api not found")

def generate_text(input):
    model=genai.GenerativeModel("gemini-pro")
    response= model.generate_content(input)
    return response.text

st.title("Google gen ai text response")
user_input=st.text_area("Enter text here")

if st.button("generate response"):
    if user_input:
        response_text= generate_text(user_input)
        if response_text:
            st.subheader("Ai response")
            st.write(response_text)
    else:
        st.error("Please enter some text")