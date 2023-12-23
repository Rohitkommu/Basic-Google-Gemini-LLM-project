from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question,stream=True)
    return response

st.set_page_config(page_title="QUESTION AND ANSWER")

st.header("Gemini LLM Application")

input=st.text_input("Input: ",key="input")
submit=st.button("Ask the Question")

if submit:
    response= get_gemini_response(input)
    
    for chunk in response:
        print(st.write(chunk.text))
        print("_"*80)
    st.write(chat.history)