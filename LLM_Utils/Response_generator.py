import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_API_KEY"],
)

def generate_reply(user_input, tone):
    completion = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3.2:novita",
        messages=[
            {
                "role": "system",
                "content": f"You are a rizz responder who talks like Gen Z in a {tone} tone"
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
    )
    return completion.choices[0].message.content


    