"""
LangChain vector store and agent setup for Autonomous Prompt-Based Assistant.
"""

import os
import pandas as pd
from dotenv import load_dotenv  # ✅ Load environment variables from .env

from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.docstore.document import Document

# ✅ Load .env variables (OPENAI_API_KEY)
load_dotenv()

# ✅ Paths
DATA_PATH = "data/raw/company_faq.csv"
VECTOR_DIR = "models/vector_store"

def load_docs():
    df = pd.read_csv(DATA_PATH)
    docs = [Document(page_content=f"Q: {row['question']}\nA: {row['answer']}") for _, row in df.iterrows()]
    return docs

def create_vector_store():
    docs = load_docs()
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = text_splitter.split_documents(docs)

    # ✅ Use OpenAI embeddings (API key loaded from .env)
    embeddings = OpenAIEmbeddings()
    vectordb = FAISS.from_documents(split_docs, embeddings)

    # ✅ Save to disk
    vectordb.save_local(VECTOR_DIR)
    return vectordb

def load_qa_chain():
    vectordb = FAISS.load_local(VECTOR_DIR, OpenAIEmbeddings())
    llm = ChatOpenAI(temperature=0.3)
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectordb.as_retriever())
    return qa

# ✅ Run if this script is executed directly
if __name__ == "__main__":
    print("📥 Creating vector store from FAQ data...")
    create_vector_store()
    print(f"✅ Vector store created and saved to: {VECTOR_DIR}")
