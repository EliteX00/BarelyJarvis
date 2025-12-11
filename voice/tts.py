import asyncio
import json
import os
from asyncio.timeouts import timeout

import numpy as np
import pyaudio
import sounddevice as sd
import websockets
from dotenv import load_dotenv

load_dotenv()

WEBSOCKET_URL = "wss://api.deepgram.com/v1/speak?model=aura-2-aries-en"
headers = {"Authorization": f"Token {os.getenv("DEEPGRAM_API_KEY")}"}


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 24000
CHUNK = 1024

websocket = None


async def tts_connect():
    global websocket
    websocket = await websockets.connect(WEBSOCKET_URL, additional_headers=headers)
    return websocket


async def speak(text):
    audio = pyaudio.PyAudio()
    stream = audio.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        output=True,
        frames_per_buffer=CHUNK,
    )

    text_payload = {"type": "Speak", "text": f"{text}"}
    await websocket.send(json.dumps(text_payload))

    flush_payload = {"type": "Flush"}
    await websocket.send(json.dumps(flush_payload))

    while True:
        message = await websocket.recv()

        if isinstance(message, bytes):

            stream.write(message)
        elif isinstance(message, str):

            try:
                control_message = json.loads(message)
                print(f"Received control message: {control_message}")
                if control_message.get("type") == "Flushed":
                    break
            except json.JSONDecodeError:
                print(f"Received non-JSON text message: {message}")
