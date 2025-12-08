# core/memory.py

from .system_instructions import SYSTEM_INSTRUCTIONS

memory = [SYSTEM_INSTRUCTIONS]

def add_to_memory(role: str, content: str):
    global memory
    memory.append({"role": role, "content": content})

    if len(memory) > 10:
        memory = [SYSTEM_INSTRUCTIONS] + memory[-10:]

def get_memory():
    return memory
