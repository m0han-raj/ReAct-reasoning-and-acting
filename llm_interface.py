import os
import requests
import json
from dotenv import load_dotenv
from time import sleep

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY not found in .env")

def call_llm(prompt, max_retries=3):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/your-repo",  # Required for free tier
        "X-Title": "ReAct Agent"  # Required for free tier
    }

    payload = {
        "model": "qwen/qwen3-235b-a22b:free",  # More reliable than Qwen free
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 500
    }

    for attempt in range(max_retries):
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=30)
            response.raise_for_status()
            data = response.json()

            if "error" in data:
                raise ValueError(data["error"]["message"])

            return data["choices"][0]["message"]["content"].strip()

        except requests.exceptions.RequestException as e:
            if attempt == max_retries - 1:
                return f"[API Error] Request failed: {str(e)}"
            sleep(1)  # Backoff before retry

        except (KeyError, json.JSONDecodeError) as e:
            return f"[Parse Error] Invalid response format: {str(e)}"

    return "[Error] Max retries exceeded"