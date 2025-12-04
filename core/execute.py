import subprocess
import time
import webbrowser

def launch(app):
    subprocess.Popen(app, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def delay_exec(seconds, func):
    def wrapper():
        time.sleep(seconds)
        func()
    return wrapper

FUNCTIONS = {
    "A101": lambda: webbrowser.open("https://instagram.com"),
    "A102": lambda: webbrowser.open("https://spotify.com"),
    "A103": delay_exec(3, lambda: subprocess.call(["reboot"])),
    "A104": lambda: launch("legacylauncher"),
}

def run_execution_code(code):
    func = FUNCTIONS.get(code)
    if callable(func):
        func()
