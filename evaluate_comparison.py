import json
import os

def evaluate_accuracy(log_file):
    if not os.path.exists(log_file):
        print(f"Log file not found: {log_file}")
        return

    total = 0
    correct = 0
    print(f"\nEvaluating results from: {log_file}")
    print("-" * 60)
    
    with open(log_file, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            question = data.get("question", "").strip()
            gold = data.get("answer", "").strip()
            pred = data.get("prediction", "").strip()
            is_correct = data.get("correct", False)

            print(f"Q: {question}")
            print(f"Gold: {gold}")
            print(f"Prediction: {pred}")
            print(f"Correct: {'✅' if is_correct else '❌'}")
            print("-" * 60)

            total += 1
            if is_correct:
                correct += 1

    accuracy = 100 * correct / total if total > 0 else 0.0
    print(f"\n📊 Accuracy: {correct}/{total} = {accuracy:.2f}%")
    return accuracy


if __name__ == "__main__":
    fever_log = "logs/fever_results.jsonl"
    hotpotqa_log = "logs/hotpotqa_results.jsonl"

    print("====== Evaluating Qwen's ReAct Performance ======")
    fever_acc = evaluate_accuracy(fever_log)
    hotpotqa_acc = evaluate_accuracy(hotpotqa_log)

    print("\n====== Summary ======")
    print(f"FEVER Accuracy:    {fever_acc:.2f}%")
    print(f"HotpotQA Accuracy: {hotpotqa_acc:.2f}%")
