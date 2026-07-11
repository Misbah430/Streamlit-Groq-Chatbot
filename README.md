## 🤖 Groq AI Chatbot

A simple AI chatbot built with **Python**, **Streamlit**, and the **Groq API**. The chatbot provides real-time conversational responses using the Llama 3.3 70B Versatile model, while maintaining a chat history throughout the session.

## 🚀 Features
* 💬 Interactive chat interface
* ⚡ Fast AI responses powered by Groq
* 📝 Chat history
* 🔐 Secure API key management using `.env`
* 🎨 Clean and responsive Streamlit UI

## 🛠️ Technologies Used
* Python 3.12
* Streamlit
* Groq API
* python-dotenv
## 📂 Project Structure
Chatbot/
│── chatbot.py
│── requirements.txt
│── .env
│── .gitignore
│── README.md

## 📦 Installation

Clone the repository:
```bash
git clone https://github.com/your-username/groq-chatbot.git
```
Go to the project folder:
```bash
cd groq-chatbot

Create a virtual environment (optional):

```bash
conda create -p chatbot python=3.12 -y
conda activate chatbot
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project folder.

Add your Groq API key:

```env
GROQ_API_KEY=your_api_key_here
```

---
![Uploading Screenshot (229).png…]()

## ▶️ Run the Application

```bash
streamlit run chatbot.py

## 📌 Future Improvements

* Multiple chat sessions
* Conversation history
* Download chat as PDF
* Theme switch (Dark/Light)
* Web search integration
* Voice input and output
* RAG using PDF documents



