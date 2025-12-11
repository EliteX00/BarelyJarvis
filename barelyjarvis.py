# jarvis.py
import asyncio
import re

from core.brain import get_ai_response
from core.execution import execute_from_ai_response
from voice.tts import speak, tts_connect


def clean_response_for_tts(ai_response: str) -> str:

    text = re.sub(r"SONG:\s*.+", "", ai_response)

    text = re.sub(r"EXECUTION_CODE:\s*A\d+", "", text)
    return text.strip()


async def main():
    while True:
        await tts_connect()
        try:
            user_query = input("User: ")
        except (EOFError, KeyboardInterrupt):
            print("\nShutting down BarelyJarvis.")
            break

        ai_response = get_ai_response(user_query)

        print(f"JARVIS: {ai_response}")

        clean_text = clean_response_for_tts(ai_response)
        if clean_text:
            await speak(clean_text)

        execute_from_ai_response(ai_response)


if __name__ == "__main__":
    asyncio.run(main())
