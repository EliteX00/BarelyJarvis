import re

def extract_execution_code(text):
    match = re.search(r"EXECUTION_CODE:\s*(A\d+)", text)
    if match:
        return match.group(1)
    return None
