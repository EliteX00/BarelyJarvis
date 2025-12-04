import subprocess
from groq import Groq

from core.memory import add, memory
from core.system_prompt import SYSTEM_INSTRUCTIONS
from core.execute import run_execution_code
from core.utils import extract_execution_code

client = Groq(api_key="YOUR_KEY_HERE")

def main():
    while True:
        user_query = input("User: ")

        add("user", user_query)

        response = client.chat.completions.create(
            messages=memory,
            model="llama-3.3-70b-versatile"
        )

        ai_response = response.choices[0].message.content

        print(f"JARVIS: {ai_response}")

        add("assistant", ai_response)

        code = extract_execution_code(ai_response)
        if code:
            run_execution_code(code)


if __name__ == "__main__":
    main()
