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

#Safety checker
def simple_safety_check(text: str) -> bool:
    blocked = ["sexual", "rape", "kill", "slur"]
    t = (text or "").lower()
    return not any(b in t for b in blocked)

import streamlit as st
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="Rizz Responder", page_icon="💬")
st.title("Rizz Responder — Beginner")

user_name = st.text_input("Your name (optional)")
situation = st.text_area("Describe the situation / paste the message", height=140)
tone = st.selectbox("Choose a tone", ["Playful", "Sweet", "Confident", "Supportive"])

if st.button("Generate response"):
    if not situation or not situation.strip():
        st.warning("Please enter the situation first.")
    else:
        # try remote
        reply = generate_remote(situation, tone, user_name)
        # try local if remote returned nothing
        if not reply:
            reply = generate_local(situation, tone, user_name)
        # fallback to templates
        if not reply:
            reply = random.choice(TEMPLATES.get(tone, ["(No reply)"]))
        # safety
        if not simple_safety_check(reply):
            st.warning("Generated reply failed safety check — showing safe fallback.")
            reply = random.choice(TEMPLATES.get(tone, ["(No safe reply)"]))
        st.subheader("Reply")
        st.write(reply)


def generate_remote(situation: str, tone: str, name: str = None) -> str:
    # placeholder: tries remote if you add HF token later
    return ""  # empty means remote not available / failed

def generate_local(situation: str, tone: str, name: str = None) -> str:
    # placeholder local generator — for now just return an empty string to force fallback
    return ""
