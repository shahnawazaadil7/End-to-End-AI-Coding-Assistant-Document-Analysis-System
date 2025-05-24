# 🤖 End-to-End GenAI Coding Assistant with DeepSeek-R1

Welcome to the **GenAI Coding Assistant**, a Streamlit-powered application that merges advanced language models with intuitive interfaces to provide:

- 💬 **AI Coding Assistant** – Your expert pair programmer.
- 📄 **DocuMind AI** – Your intelligent assistant for document summarization and contextual Q&A.

Built using the **DeepSeek-R1 1.5B** model via **Ollama**, this tool is ideal for developers, researchers, and learners.

---

## 🚀 Features

### 🧠 GenAI Coding Assistant
- Supports Python, JavaScript, C++, and more.
- Gives structured explanations and optimized code suggestions.
- Offers debugging strategies and best practices.
- Interactive, multi-turn conversational memory.

### 📘 DocuMind AI – Document Analysis
- Upload and query documents in formats like `.pdf`, `.docx`, `.txt`, `.csv`, `.xlsx`, `.pptx`.
- Summarizes content and answers context-aware questions.
- Uses LangChain for chunking, vector storage, and querying.

### 🧾 Clean UI
- Streamlit-based layout with easy navigation.
- Modular code structure: `ui.py`, `chat.py`, `docu.py`.

---

## 🧩 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **LLM Backend**: [Ollama](https://ollama.com/) with `deepseek-r1:1.5b`
- **LangChain**: For document loading, chunking, embeddings, and prompt chaining
- **Vector Store**: In-memory vector search
- **File Support**: PDF, Word, Text, Excel, CSV, PowerPoint

---

## 📦 Installation

1. **Clone the Repository**
```bash
   git clone https://github.com/shahnawazaadil7/genai-coding-assistant.git
   cd genai-coding-assistant
   ```

2.	Set Up Python Environment

```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt

```
3.	Install and Start Ollama
•	Install Ollama
•	Run:
```
   ollama run deepseek-r1:1.5b
```

4.	Run the Streamlit App
```
   streamlit run main.py
```


⸻

📁 File Structure
```
├── main.py                 # Entry point with routing UI
├── chat.py                 # Coding assistant logic
├── docu.py                 # Document analysis logic
├── ui.py                   # UI styling and page structure
├── requirements.txt        # Python dependencies
├── README.md               # Project description
└── documents/              # Directory for uploaded documents
```

⸻

🛠️ To-Do
	•	Add support for external vector stores like FAISS or Chroma
	•	Enable multi-file uploads
	•	Add conversation history export
	•	Deploy via Docker

⸻

🧠 Model Info

This app uses DeepSeek-R1 1.5B via Ollama – a powerful open-source LLM fine-tuned for reasoning and coding.

⸻

📝 License

This project is licensed under the MIT License. Feel free to use, modify, and share it.

⸻

🙌 Acknowledgements
	•	Streamlit
	•	Ollama
	•	LangChain
	•	DeepSeek

⸻

💡 Author

Made with ❤️ by Shahnawaz Aadil

Let me know if you'd like a version with deployment instructions (Docker/Cloud) or a `requirements.txt` file.
