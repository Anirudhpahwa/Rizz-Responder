import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
from huggingface_hub import InferenceClient

HF_API_KEY = os.getenv("HF_API_KEY")
client = InferenceClient(api_key=HF_API_KEY) if HF_API_KEY else None

if not HF_API_KEY:
    st.warning("HF_API_KEY not found. Add it to .env to use AI. App will use local templates as fallback.")
