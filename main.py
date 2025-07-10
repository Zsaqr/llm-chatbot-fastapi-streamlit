import os
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
print("API KEY:", OPENROUTER_API_KEY)


class Message(BaseModel):
    user_input: str

@app.post("/chat")
async def chat_endpoint(message: Message):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "ZiadChatbot"
    }

    data = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [
         {"role": "user", "content": message.user_input}
        ]
    }


    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=data
    )

    if response.status_code == 200:
        result = response.json()
        reply = result['choices'][0]['message']['content']
        return {"response": reply}
    else:
        return {"error": "Failed to get response", "details": response.text}
