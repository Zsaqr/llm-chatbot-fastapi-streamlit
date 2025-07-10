
# 🤖 LLM Chatbot with FastAPI & Streamlit

A simple chatbot powered by a real LLM (via OpenRouter API), with a FastAPI backend and a Streamlit chat interface.

---

## 📸 Demo

![screenshot](https://via.placeholder.com/800x400?text=Insert+Screenshot+Here)

---

## 🚀 Features

- 🔌 **Backend** with FastAPI – Handles requests and connects to OpenRouter's LLM API.
- 🖥️ **Frontend** with Streamlit – Chat interface with persistent message history.
- 💾 **Chat history** – Saved to a JSON file after every message.
- 🧹 **Clear chat** – Reset conversation with a button.
- 📦 **Deployable** as a local app or `.exe` file.
- ☁️ **Ready for deployment** to Streamlit Cloud or Render.

---

## 📁 Project Structure

```
llm-chatbot/
│
├── app.py                 # Streamlit frontend
├── main.py                # FastAPI backend
├── launch.py              # Optional launcher script
├── chat_history_*.json    # Saved chats
├── .env                   # Contains your API key
├── requirements.txt       # Project dependencies
└── README.md              # You're reading it!
```

---

## 🧪 How to Run Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Add your OpenRouter API key

Create a `.env` file in the root folder:

```
OPENROUTER_API_KEY=sk-xxxxxxx
```

---

### 3. Run the backend (FastAPI)

```bash
uvicorn main:app --reload
```

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to test the backend.

---

### 4. Run the frontend (Streamlit)

In a new terminal:

```bash
streamlit run app.py
```

The chatbot will open in your browser at [http://localhost:8501](http://localhost:8501)

---

## 🔧 Optional Enhancements

- Convert to `.exe` with [auto-py-to-exe](https://pypi.org/project/auto-py-to-exe/)
- Add user authentication
- Store history in a database
- Deploy online (Streamlit Cloud / Render / Railway)

---

## 📄 License

MIT License

---

## 👤 Author

**Ziad Muhammed Saqr**  
Machine Learning & AI Developer  
📧 ziad@example.com *(replace with your real email)*
