import random

from backend_server.utils.prompt_templates import generate_prompt


def get_payload(message):
    return {
        "inputs": generate_prompt(message),
        "parameters": {
            "return_full_text": False,
            "temperature": round(random.uniform(0.7, 0.9), 2)
        }
    }
