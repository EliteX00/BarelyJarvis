# voice/tts.py

import json
import os
import time
import wave

import websocket
import _thread 

DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY", "")

global_ws = None
global_wf = None

def init_tts_connection():
    """
    Initialize Deepgram Aura-2 Aries TTS over WebSocket.
    """
    global global_ws, global_wf

    if not DEEPGRAM_API_KEY:
        print("[WARN] DEEPGRAM_API_KEY is not set. TTS will not work.")
        return

    WS_URL = (
        "wss://api.deepgram.com/v1/speak?"
        "model=aura-2-aries-en&encoding=linear16&sample_rate=16000"
    )

    AUDIO_FILE = "output.wav"

    global_wf = wave.open(AUDIO_FILE, "wb")
    global_wf.setnchannels(1)
    global_wf.setsampwidth(2)
    global_wf.setframerate(16000)

    headers = [f"Authorization: Token {DEEPGRAM_API_KEY}"]

    def on_open(ws):
        print("[TTS] WebSocket connected.")

    def on_message(ws, message):
        global global_wf

        if isinstance(message, bytes):
            global_wf.writeframes(message)
        else:
            print("[TTS JSON]", message)

        if isinstance(message, str) and '"Flushed"' in message:
            global_wf.close()
            os.system("mpv output.wav")

            global_wf = wave.open("output.wav", "wb")
            global_wf.setnchannels(1)
            global_wf.setsampwidth(2)
            global_wf.setframerate(16000)

    def on_close(ws, *_):
        print("[TTS] WebSocket closed — reconnecting…")
        time.sleep(1)
        init_tts_connection()

    global_ws = websocket.WebSocketApp(
        WS_URL,
        header=headers,
        on_open=on_open,
        on_message=on_message,
        on_close=on_close,
    )

    _thread.start_new_thread(global_ws.run_forever, ())

def tts_aries(text: str):
    """
    Send text to Deepgram TTS over WebSocket.
    """
    global global_ws

    if not DEEPGRAM_API_KEY:
        print("[TTS] Skipping, no DEEPGRAM_API_KEY set.")
        return

    if global_ws:
        global_ws.send(json.dumps({"type": "Speak", "text": text}))
        global_ws.send(json.dumps({"type": "Flush"}))
    else:
        print("[TTS] WebSocket not ready.")
