# 🤖 Groq AI Chatbot

A simple and responsive AI chatbot built with **Python**, **Streamlit**, and the **Groq API**. The chatbot uses the **Llama 3.3 70B Versatile** model to generate fast, real-time AI responses.

---

## 📌 Features

- 🤖 Powered by Groq API
- 🧠 Uses Llama 3.3 70B Versatile model
- 💬 Interactive chat interface
- ⚡ Real-time streaming responses
- 📝 Automatic conversation title
- 🆕 Start a new conversation
- 📥 Download chat history as JSON
- 🔒 Secure API key management using `.env`
- 🎨 Clean and responsive Streamlit interface

---

## 🖼️ Preview

<img width="1364" height="670" alt="Screenshot " src="https://github.com/user-attachments/assets/f4cdbb0c-e95e-44fe-b777-bd93538b60ef" />


Example:

![Groq AI Chatbot](
)

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Groq API
- Llama 3.3 70B Versatile
- python-dotenv

---

## 📁 Project Structure

```text
Streamlit-Groq-Chatbot/
│── chat.py
│── requirenments.txt
│── .env
│── .gitignore
│── README.md
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/Misbah430/Streamlit-Groq-Chatbot.git
```

### Navigate to the project folder

```bash
cd Streamlit-Groq-Chatbot
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key
```

### Run the application

```bash
streamlit run app.py
```

---

## 💡 How It Works

1. Enter your question in the chat box.
2. The chatbot sends your prompt to the Groq API.
3. Responses are streamed in real time.
4. The first prompt becomes the conversation title.
5. Start a new chat or download the conversation whenever you like.

---

## 📦 Requirements

```
streamlit
groq
python-dotenv
```

---


## ⭐ Future Improvements

- Multiple chat history
- Copy response button
- Regenerate response
- Model selection from sidebar
- Export conversation as PDF
- Light/Dark theme switch

---
