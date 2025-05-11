from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

MODEL_NAME = "HealthML/ChatDoctor"

# Load tokenizer and model once, upon import
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

def ask_ai(symptoms: str) -> str:
    # Encode input text
    inputs = tokenizer.encode(symptoms, return_tensors="pt")

    # Generate a response, limit tokens to avoid very long outputs
    with torch.no_grad():
        outputs = model.generate(inputs, max_length=100, do_sample=True, top_p=0.95, top_k=50)

    # Decode the output tokens to string
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return response
