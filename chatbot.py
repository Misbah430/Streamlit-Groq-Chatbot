#conda activate D:\Miniconda\conda\Chatbot\chatbot
import os
import json
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

st.set_page_config(
    page_title="Groq AI Chatbot",
    page_icon="🤖",
    layout="wide"
)
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("GROQ_API_KEY not found!")
    st.stop()

client = Groq(api_key=api_key)

SYSTEM_PROMPT = {
    "role": "system",
    "content": """
You are Groq AI Chatbot, created by Misbah.

- If asked about your technology, say:
  "I use the Llama 3.3 70B language model through the Groq API."

- Be friendly, accurate, and helpful.
"""
}

if "messages" not in st.session_state:
    st.session_state.messages = [SYSTEM_PROMPT]

if "chat_title" not in st.session_state:
    st.session_state.chat_title = "New Conversation"


st.title("🤖 Groq AI Chatbot")
st.caption("Let's Talk")
st.sidebar.caption("Model")
st.sidebar.success("Llama 3.3 70B")

with st.sidebar:

    st.header("💬 Chat")

    st.write(f"**Current Chat:**")
    st.info(st.session_state.chat_title)

    if st.button("🗑️ New Chat", use_container_width=True):

        st.session_state.messages = [SYSTEM_PROMPT]
        st.session_state.chat_title = "New Conversation"
        st.rerun()

    st.download_button(
        "⬇️ Download Conversation",
        data=json.dumps(
            st.session_state.messages,
            indent=4
        ),
        file_name="conversation.json",
        mime="application/json",
        use_container_width=True
    )

for msg in st.session_state.messages:

    if msg["role"] == "system":
        continue

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Ask me anything...")

if prompt:

    if len(st.session_state.messages) == 1:
        st.session_state.chat_title = (
            prompt[:40] + "..."
            if len(prompt) > 40
            else prompt
        )

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        placeholder = st.empty()
        full_response = ""

        try:

            stream = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=st.session_state.messages,
                temperature=0.7,
                max_tokens=2048,
                stream=True
            )

            for chunk in stream:

                content = chunk.choices[0].delta.content or ""

                full_response += content

                placeholder.markdown(full_response + "▌")

            placeholder.markdown(full_response)

        except Exception as e:

            full_response = f"⚠️ {e}"

            placeholder.error(full_response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": full_response
        }
    )
    