import json

def load_data():
    with open("data/hotpotqa.json") as f:
        data = json.load(f)
        for item in data:
            yield{
                "context": item["context"],
                "question": item["question"],
                "answer":item.get("answer","")            
            }