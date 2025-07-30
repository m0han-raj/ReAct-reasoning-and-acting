def get_prompt(context, question, history):
    history_text = "\n".join(history)
    return f"""Answer the following question using the ReAct framework. Format your response EXACTLY as shown:

Context: {context}

Question: {question}

{history_text}

You MUST respond in this format:
Thought [number]: [your reasoning]
Act [number]: [Search/Lookup/Finish][query]
Observation [number]: [result will be provided]
"""