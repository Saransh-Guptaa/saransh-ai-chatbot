import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

st.set_page_config(
    page_title="Saransh AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Saransh's AI Chatbot")
st.caption("Powered by Google Gemini · Built by Saransh Gupta")

if "chat" not in st.session_state:
    model = genai.GenerativeModel("gemini-2.0-flash")
    st.session_state.chat = model.start_chat(history=[])

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
            try:
                response = st.session_state.chat.send_message(prompt)
                reply = response.text
                st.markdown(reply)
                st.session_state.messages.append(
                    {"role": "assistant", "content": reply}
                )
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.info("Please check your API key in settings.")
