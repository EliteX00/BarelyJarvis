# integrations/launcher.py

import subprocess
import time

def launch(app: str):
    subprocess.Popen(app, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def delay_exec(seconds: int, func):
    def wrapper():
        time.sleep(seconds)
        func()
    return wrapper
