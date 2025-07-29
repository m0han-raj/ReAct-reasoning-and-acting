from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import transformers
transformers.logging.set_verbosity(transformers.logging.CRITICAL)

# Load Qwen 1.5 model locally
model_id = "Qwen/Qwen1.5-1.8B"  # or "Qwen/Qwen1.5-4B" if you have enough GPU

tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True)
model.eval()
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

def call_llm(prompt):
    inputs = tokenizer(prompt, return_tensors="pt",padding=True).to(device)
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=50,
            pad_token_id=tokenizer.pad_token_id,
            do_sample=True,
            temperature=0.7,
            top_p=0.9
        )
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return result
