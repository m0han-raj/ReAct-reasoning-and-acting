import json 

def load_data():
    with open("data/fever.json") as f:
        data = json.load(f)
        for item in data:
            yield {
                "context": item["context"],
                "claim": item["claim"],
                "label": item.get("label", "")
            }