from agent import ReActAgent
from environments import hotpotqa_env, fever_env
from utils import log_result

def run_environment(env_loader, env_name):
    env = env_loader.load_data()
    agent = ReActAgent(env_name)
    results=[]
    for sample in env:
        result = agent.run(sample)
        log_result(env_name, sample, result)
        results.append(result)
    return results

    total = len(results)
    correct = sum(1 for r in results if r.get("correct", False))
    print(f"[{env_name}] Accuracy: {correct}/{total} = {100 * correct / total:.2f}%")

if __name__ == "__main__":
    print("Running HotpotQA...")
    run_environment(hotpotqa_env, "hotpotqa")
    print("Running FEVER...")
    run_environment(fever_env, "fever")


