# core/brain.py

import os

from dotenv import load_dotenv
from groq import Groq

from .memory import add_to_memory, get_memory

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

if not GROQ_API_KEY:
    print("[WARN] GROQ_API_KEY is not set. Jarvis will not be able to respond.")

client = Groq(api_key=GROQ_API_KEY)


def get_ai_response(user_query: str) -> str:
    add_to_memory("user", user_query)

    chat_completion = client.chat.completions.create(
        messages=get_memory(),
        model="llama-3.3-70b-versatile",
    )
    ai_response = chat_completion.choices[0].message.content

    add_to_memory("assistant", ai_response)
    return ai_response
