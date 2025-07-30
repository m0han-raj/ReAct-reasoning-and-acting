import json
import os
from agent import ReActAgent
from environments.fever_env import load_dataset_f
from environments.hotpotqa_env import load_dataset_h

def generate_predictions(agent, dataset, output_file):
    results = []

    for i, sample in enumerate(dataset):
        try:
            print(f"\n{'='*60}\nProcessing Sample {i+1}:")
            print(f"Question: {sample['question']}")

            output = agent.run(sample)
            print(f"\nAgent Steps:\n{output}")
            if "Finish[" in output:
                pred = output.split("Finish[")[-1].split("]")[0]
            else:
                pred = "N/A"

            results.append({
                "question": sample["question"],
                "answer": sample["answer"],
                "prediction": pred,
                "steps": agent.steps
            })

        except Exception as e:
            print(f"[!] Error processing sample {i+1}: {e}")
            continue

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", encoding='utf-8') as f:
        for r in results:
            f.write(json.dumps(r) + "\n")

    print(f"\n[✓] Predictions saved to: {output_file}")

if __name__ == "__main__":
    agent = ReActAgent()

    hotpotqa_data = list(load_dataset_h("data/hotpotqa.json",limit=100))
    generate_predictions(agent, hotpotqa_data, "data/logs/hotpotqa_results.jsonl")

    fever_data = list(load_dataset_f("data/fever.json",limit=10))  
    generate_predictions(agent, fever_data, "data/logs/fever_results.jsonl")

