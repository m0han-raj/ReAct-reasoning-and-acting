import json

def load_dataset_h(file_path, limit=4):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

        for i, item in enumerate(data):
            if i >= limit:
                break

            if "question" not in item or "context" not in item:
                continue
            context = " ".join(
                sentence
                for paragraph in item["context"]
                for sentence in paragraph[1]
            )

            yield {
                "context": context,
                "question": item["question"],
                "answer": item.get("answer", "")
            }
