import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
from huggingface_hub import InferenceClient

HF_API_KEY = os.getenv("HF_API_KEY")
client = InferenceClient(api_key=HF_API_KEY) if HF_API_KEY else None

if not HF_API_KEY:
    st.warning("HF_API_KEY not found. Add it to .env to use AI. App will use local templates as fallback.")

#Fallback
TEMPLATES = {
    "Playful": ["That’s cheeky — I like it.", "Careful, I might flirt back 😉"],
    "Sweet": ["That warmed my day. Tell me more.", "You have such a sweet way with words."],
    "Confident": ["I like that—coffee this week?", "Bold move. I respect it."],
    "Supportive": ["I’m here for you if you want to talk.", "That sounds hard — I’m listening."]
}
def build_prompt(situation: str, tone: str, name: str = None) -> str:
    prompt = f"You are a friendly assistant. Tone: {tone}\n Situation: {situation}\n Write 1-2 short, respectful lines."
    if name:
        prompt += f" Use the name: {name}."
    return prompt
