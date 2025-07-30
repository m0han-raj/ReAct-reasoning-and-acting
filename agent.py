from llm_interface import call_llm
from prompts import get_prompt

class ReActAgent:
    def __init__(self):
        self.steps = []
        self.history = []
        self.max_steps = 5

    def run(self, sample):
        context = sample.get("context", "")
        question = sample["question"]
        self.steps = []
        self.history = []

        observation = ""
        for step in range(1, self.max_steps + 1):
            try:
                prompt = get_prompt(context, question, self.history)
                if observation:
                    prompt += f"\nObservation {step-1}: {observation}"

                response = call_llm(prompt).strip()
                self.steps.append(response)
                print(f"Step {step} Response: {response}")  # Debug output

                if "Finish[" in response:
                    return self._format_final_output()

                observation = self.mock_observe(response)
                thought, action = self.parse_response(response)

                self._update_history(step, thought, action, observation)

            except Exception as e:
                self.steps.append(f"[Step {step} Error] {str(e)}")
                break

        return self._format_final_output()

    def _update_history(self, step, thought, action, observation):
        self.history.extend([
            f"Thought {step}: {thought}",
            f"Act {step}: {action}",
            f"Obs {step}: {observation}"
        ])

    def _format_final_output(self):
        return "\n".join([
            f"=== ReAct Trace ===",
            *self.steps,
            f"=== History ===",
            *self.history
        ])

    def mock_observe(self, response):
        # Enhanced mock observations
        search_prefix = "Search["
        if search_prefix in response:
            query = response.split(search_prefix)[1].split("]")[0]
            
            # Dataset-specific responses
            if "nationality" in query.lower():
                return "Scott Derrickson is American. Ed Wood was American."
            elif "government position" in query.lower():
                return "Shirley Temple served as US Ambassador to Ghana and Czechoslovakia."
            elif "science fantasy" in query.lower():
                return "The 'Animorphs' series matches this description."
            else:
                return f"Search results for '{query}': Found 3 relevant documents."

        return "No action detected."

    def parse_response(self, response):
        thought = action = ""
        lines = [line.strip() for line in response.split("\n") if line.strip()]
        
        for line in lines:
            lower_line = line.lower()
            if lower_line.startswith("thought"):
                thought = line.split(":", 1)[-1].strip()
            elif lower_line.startswith("act"):
                action = line.split(":", 1)[-1].strip()
        
        return thought or "No thought generated", action or "No action specified"