import json

def load_dataset_f(file_path, limit=100):
    with open(file_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i >= limit:
                break
            try:
                item = json.loads(line)
                yield {
                    "context": "",  # FEVER base version lacks full article context
                    "question": item.get("claim", ""),  # this is the 'question'
                    "answer": item.get("label", "")     # expected label: SUPPORTS, REFUTES, etc.
                }
            except Exception as e:
                print(f"[!] Error processing sample {i + 1}: {e}")
