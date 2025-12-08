# core/execution.py

import os
import re
import webbrowser

from integrations.launcher import delay_exec, launch
from integrations.spotify import spotify_play

FUNCTIONS = {
    "A101": lambda: webbrowser.open("http://instagram.com"),
    "A102": lambda: webbrowser.open("https://spotify.com"),
    "A103": delay_exec(3, lambda: webbrowser.open("http://instagram.com")),
    "A104": lambda: launch("legacylauncher"),
    "A105": lambda: os.system("hyprshot -m output -m VGA-1"),
}

def execute_from_ai_response(ai_response: str):
    match = re.search(r"EXECUTION_CODE:\s*(A\d+)", ai_response)
    if not match:
        return

    code = match.group(1).strip()

    if code == "A106":
  
        spotify_play(ai_response)
        return

    func = FUNCTIONS.get(code)
    if callable(func):
        func()
