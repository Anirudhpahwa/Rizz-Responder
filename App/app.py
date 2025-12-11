import streamlit as st
from llm_utils.Response_generator import generate_reply

st.set_page_config(page_title="Rizz Responder", page_icon="💬")

st.title("💬 Rizz Responder")

st.write("Enter a message and let the AI craft the perfect reply.")

# Input field
user_input = st.text_area("Message:", placeholder="Type something...")

# Optional tone selector
tone = st.selectbox(
    "Select tone:",
    ["Playful", "Sweet", "Confident", "Supportive", "Angry"],
    index=0
)

# Button to generate response
if st.button("Generate Response"):
    if not user_input.strip():
        st.warning("Please enter a message first.")
    else:
        with st.spinner("Crafting your rizz..."):
            try:
                response = generate_reply(user_input, tone=tone)
                st.success(response)
            except Exception as e:
                st.error(f"Error generating response: {e}")
