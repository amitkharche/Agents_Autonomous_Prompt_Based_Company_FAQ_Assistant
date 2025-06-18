"""
Streamlit frontend for company-specific assistant using LangChain agent.
"""

# ✅ MUST BE FIRST Streamlit command
import streamlit as st
st.set_page_config(page_title="🤖 Company Assistant", layout="centered")

# ✅ Set import path for src/ module
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ✅ Load environment variables from .env if available
from dotenv import load_dotenv
load_dotenv()

# ✅ Step 1: Check for API key in environment
openai_key = os.getenv("OPENAI_API_KEY")

if openai_key:
    from src.agent import load_qa_chain

    st.title("🤖 Ask your Company Assistant")
    qa_chain = load_qa_chain()

    query = st.text_input("What would you like to know?")
    if query:
        with st.spinner("Thinking..."):
            response = qa_chain.run(query)
        st.success("Response:")
        st.write(response)
else:
    st.error("❌ OpenAI API key not found. Please make sure `.env` file exists and contains a valid `OPENAI_API_KEY`.")
