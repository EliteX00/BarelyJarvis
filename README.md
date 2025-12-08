# BarelyJarvis 
Welcome to BarelyJarvis my totally serious attempt to build a jarvis-like system even though i have my budget and sleep schedule hanging by a thread.

Right now i am building the software part, because i dont have the hardware yet - thats exactly why m applying for Hack Club $400 Grant

Yes this entire project is held together by hopes, dreams, and API keys

# what barelyjarvis can do right now (somehow)
- talks in jarvis style
- has memory (like 10 message)
- opens apps using secret execution codes
- uses Groq Llama 3.3 for fast replies
- suggests and open spotify songs

 Basically its jarvis but barely jarvis

 # voice mode (TTS Ready, STT in Development)
BarelyJarvis can now speak with an actual voice and everything

# Text-to-Speech(TTS) - READY
  - Powered by Deepgram’s Aura-2 Aries TTS model through their WebSocket API. It streams audio in real time so he responds faster than my brain

# Speech-to-Text - IN DEVELOPMENT
  - still wiring it up. Coming soon so that BarelyJarvis can listen to me instead of waiting for me to type for centuries

# Holomat UI Plan (just dreams for now)
The final setup won’t be a normal screen
I am building a projected control surface inspired by sci-fi holo-tables

The plan:

- a mini projector projects the UI onto a matte-black vinyl surface
- under the vinyl will be a capacitive touch layer
- under that is a desk mat acting as the base
- a webcam handles gesture/presence detection
- UI shows: widgets, reactive speech circle, shortcuts, etc

In other words:
```bash
Projector → Vinyl → Touch Film → Desk Mat → Table → Jarvis vibes
```

Its basically Tony Stark tech if Tony Stark had a empty wallet and bad WiFi

# how to run (if u dare)
1. install deps
    ```bash
    $ pip install -r requirements.txt
    ```
2. add your API keys into the code (u will figure it out.... hopefully)
3. run it
  ```bash
    $ python3 barelyjarvis.py
  ```
4. Ask things like:
   - "open spotify”
   - “suggest a song”
   - “run diagnostics”
   - “jarvis what is life”
5. pray it dont crash

# Current Status
- AI brain: ✔️
- TTS voice: ✔️
- STT hearing: 🔧 soon
- Holomat UI: still in imaginations
- BarelyJarvis: alive... somehow
