
---

# 🤖 Autonomous Prompt-Based Company FAQ Assistant

A fully functional **Agentic AI assistant** that leverages **LangChain**, **OpenAI GPT**, and **FAISS** to answer company-specific questions from an internal FAQ file — all through an intuitive **Streamlit interface**.

---

## 📌 Business Case

Organizations often maintain internal knowledge bases (FAQs, HR docs, IT policies). Manually searching through these can be time-consuming.

This assistant solves that by enabling:

* Fast, conversational access to FAQs
* GPT-generated human-like responses
* Zero need for manual rule-based systems

---

## 💡 Features

* 🔗 Built with **LangChain RetrievalQA + OpenAI Chat Model**
* 💬 Ask natural questions through **Streamlit**
* 🧠 Uses **FAISS vector search** over custom company FAQs
* 🧾 Loads Q\&A from `company_faq.csv`
* 🔐 Secure API key handling using `.env`
* 🛠️ Easily extendable to PDFs, DOCX, or enterprise databases

---

## 🧪 Example Query

```text
What are the working hours?
```

→ The assistant retrieves the relevant document using FAISS and crafts a natural response using GPT.

---

## 🚀 Quickstart

### ✅ 1. Install dependencies

```bash
pip install -r requirements.txt
```

### ✅ 2. Add your OpenAI API key in `.env`

Create a file named `.env` in the root directory:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### ✅ 3. Prepare the vector store (one-time step)

```bash
python src/model_training.py
```

This will:

* Load your FAQ CSV
* Create embeddings using OpenAI
* Save the FAISS index locally

### ✅ 4. Launch the assistant

```bash
streamlit run app/app.py
```

Your browser will open to a chat interface. Ask any question from your FAQ.

---

## 🐳 Docker Support (Optional)

You can containerize the assistant like this:

```bash
docker build -t company-assistant .
docker run -p 8501:8501 company-assistant
```

Make sure to pass your OpenAI key via Docker environment or bind the `.env` file.

---

## 📂 Project Structure

```
Agents_autonomous_prompt_assistant/
├── app/
│   └── app.py                  # Streamlit interface
├── data/
│   └── raw/
│       └── company_faq.csv     # Custom company FAQs
├── models/
│   └── vector_store/           # FAISS index + metadata
├── src/
│   ├── agent.py                # LangChain RetrievalQA loader
│   └── model_training.py       # Data → embeddings → FAISS
├── .env                        # API key (not committed)
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

---

## 🛠 Tech Stack

| Component      | Description                                |
| -------------- | ------------------------------------------ |
| **LangChain**  | Framework for building LLM pipelines       |
| **OpenAI GPT** | Response generation via `ChatOpenAI`       |
| **FAISS**      | Local vector store for document similarity |
| **Streamlit**  | Frontend chat interface                    |
| **Pandas**     | Data ingestion and formatting              |
| **dotenv**     | Secure API key management                  |

---

## 🔄 Future Enhancements

* Upload & ingest PDFs and Word documents
* Add memory for follow-up questions
* Track user sessions and chat logs
* Include source references or confidence scores

---
Let's Connect

Have questions or ideas for collaboration?

* [LinkedIn](https://www.linkedin.com/in/amitkharche)
* [Medium](https://medium.com/@amitkharche)
* [GitHub](https://github.com/amitkharche)

---
