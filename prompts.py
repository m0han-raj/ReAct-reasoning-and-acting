def get_prompt(context , question):
    return f"""Answer the followuing questions based on the context :

    Context: {context}

    Question: {question}

think step by step and provide a final answer"""