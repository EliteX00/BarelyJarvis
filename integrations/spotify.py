# integrations/spotify.py

import base64
import os
import re
import time
import webbrowser

import requests
from dotenv import load_dotenv

load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "")


def get_spotify_token():
    if not SPOTIFY_CLIENT_ID or not SPOTIFY_CLIENT_SECRET:
        print("[WARN] Spotify client ID/secret not set. Skipping Spotify features.")
        return None

    auth = f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}"
    auth_b64 = base64.b64encode(auth.encode()).decode()

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {auth_b64}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {"grant_type": "client_credentials"}

    r = requests.post(url, headers=headers, data=data)

    if r.status_code != 200:
        print("TOKEN ERROR:", r.text)
        return None

    return r.json().get("access_token")


def track_search(query: str):
    token = get_spotify_token()
    if not token:
        return None

    url = "https://api.spotify.com/v1/search"
    headers = {"Authorization": f"Bearer {token}"}
    params = {"q": query, "type": "track", "limit": 1}

    r = requests.get(url, headers=headers, params=params)
    data = r.json()

    if "error" in data:
        print("SPOTIFY ERROR:", data["error"])
        return None

    tracks = data.get("tracks", {}).get("items", [])
    if not tracks:
        print("No tracks found.")
        return None

    return tracks[0]


def spotify_play(ai_response: str):
    match = re.search(r"SONG:\s*(.+)", ai_response)
    if not match:
        return

    song_name = match.group(1).strip()
    track = track_search(song_name)
    if not track:
        return

    url = track["external_urls"]["spotify"]
    webbrowser.open(url)
