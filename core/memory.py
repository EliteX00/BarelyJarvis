from .system_prompt import SYSTEM_INSTRUCTIONS

memory = [SYSTEM_INSTRUCTIONS]

def add(role, content):
    global memory
    memory.append({"role": role, "content": content})

    # keep last 10 messages only
    if len(memory) > 10:
        memory = [SYSTEM_INSTRUCTIONS] + memory[-10:]
