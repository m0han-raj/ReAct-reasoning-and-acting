from llm_interface import call_llm
from prompts import get_prompt

class ReActAgent:
    def __init__(self, environment):
        self.environment = environment

    def run(self,data):
        context = data["context"]
        question = data["question"]
        prompt = get_prompt(context, question)
        response = call_llm(prompt)
            
        return {
            "queestion": question,
            "response": response,
            "answer": data.get("answer",None)
        }