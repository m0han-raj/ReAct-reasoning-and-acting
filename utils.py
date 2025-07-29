import os
import json

def log_result(env_name, data, result):
    log_path = f"data/logs/{env_name}_results.jsonl"
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    with open(log_path, "a") as f:
        log_entry = {
            "question": data["question"],
            "answer": data["answer"],
            "response": result["response"]
        }
        f.write(json.dumps(log_entry) + "\n")