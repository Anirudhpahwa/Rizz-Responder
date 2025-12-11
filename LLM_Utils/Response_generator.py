import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_API_KEY"],
)

completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3.2:novita",
    messages=[
        {
            "role": "system",
            "content": "You are a rizz responder who talks like Gen Z"
        },
        {
            "role": "user",
            "content": "My dog just died"
        }
    ],
)

print(completion.choices[0].message)