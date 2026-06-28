# 🔍 AI Web Search Agent

An intelligent AI-powered web search agent that searches the internet in real-time to answer any question. Built with LangChain, LangGraph, Groq, and Tavily.

## 🚀 Live Demo
👉 [Try it here](https://ai-web-search-agent-e92nobzvdmv7kqwahguzzs.streamlit.app/)

---

## 📌 What It Does

- Accepts any question from the user
- Decides whether to search the internet or answer directly
- Uses **Tavily** to fetch real-time web results
- Generates a clear, structured answer using **Groq LLM**
- Remembers conversation history across messages

---

## 🧠 How It Works

```
User asks question
        ↓
   ReAct Agent (Think → Act → Observe)
        ↓
   Does it need to search? 
   YES → Tavily Search → Results → LLM → Answer
   NO  → LLM answers directly
        ↓
   Streamlit displays answer
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| 🦜 LangChain | Agent framework |
| 🔁 LangGraph | ReAct agent loop |
| ⚡ Groq (llama-3.1-8b-instant) | LLM brain |
| 🔍 Tavily API | Real-time web search |
| 🧠 InMemorySaver | Conversation memory |
| 🖥️ Streamlit | Frontend UI |
| 🐍 Python | Backend logic |

---

## 📁 Project Structure

```
ai-web-search-agent/
├── agent.py          # Agent logic (LLM + Tools + Memory)
├── app.py            # Streamlit frontend
├── requirements.txt  # Project dependencies
└── .env              # API keys (not pushed to GitHub)
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/AbdulHaseeb790/ai-web-search-agent.git
cd ai-web-search-agent
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up API keys
Create a `.env` file in the root folder:
```
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

### 4. Run the app
```bash
streamlit run app.py
```

---

## 🔑 API Keys Required

| API | Get it here |
|-----|------------|
| Groq API | [console.groq.com](https://console.groq.com) |
| Tavily API | [tavily.com](https://tavily.com) |

Both are **free to get!**

---

## 💡 Features

- ✅ Real-time internet search
- ✅ Conversation memory (remembers chat history)
- ✅ ReAct agent (Think → Act → Observe loop)
- ✅ Clean Streamlit chat UI
- ✅ System prompt for focused responses
- ✅ Deployed and publicly accessible

---

## 🎯 Use Cases

- Get latest news and current events
- Research any topic in real-time
- Ask questions that require up-to-date information
- General Q&A with memory

---

## 👨‍💻 Author

**Abdul Haseeb**
- GitHub: [@AbdulHaseeb790](https://github.com/AbdulHaseeb790)
- HuggingFace: [@Haseebaidev](https://huggingface.co/Haseebaidev)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
