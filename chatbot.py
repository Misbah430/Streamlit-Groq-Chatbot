#conda activate D:\Miniconda\conda\Chatbot\chatbot
import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq
# Load environment variables
load_dotenv()
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 Groq AI Chatbot")
if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("💬 Chat History")

    if st.button("🗑️ New Chat"):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    if st.session_state.messages:
        for i, msg in enumerate(st.session_state.messages):
            if msg["role"] == "user":
                text = msg["content"]

                if len(text) > 35:
                    text = text[:35] + "..."

                st.write(f"**{i//2 + 1}.** {text}")
    else:
        st.write("No chats yet.")
# Create chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask me anything...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)
    # Send conversation to Groq
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state.messages
    )

    reply = response.choices[0].message.content

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )
    with st.chat_message("assistant"):
        st.markdown(reply)