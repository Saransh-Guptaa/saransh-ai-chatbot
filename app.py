import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(
    page_title="Saransh AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Saransh's AI Chatbot")
st.caption("Powered by Google Gemini · Built by Saransh Gupta")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = model.generate_content(prompt)
            reply = response.text
            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
