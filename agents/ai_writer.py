# agents/ai_writer.py
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

# Use open-access lightweight model
model_name = "tiiuae/falcon-rw-1b"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def spin_chapter(text: str) -> str:
    prompt = f"Rewrite the following paragraph in a more engaging and professional style:\n\n{text}\n\nRewritten:"
    output = generator(prompt, max_length=512, do_sample=True, top_k=50, top_p=0.95, temperature=0.8)
    return output[0]['generated_text'].split("Rewritten:")[-1].strip()
