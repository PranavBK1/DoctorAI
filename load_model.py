from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load BioGPT model from Hugging Face
model_name = "microsoft/BioGPT"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def ask_ai(symptoms: str) -> str:
    # Improved prompt for more accurate medical inference
    prompt = (
        f"Given the symptoms: {symptoms}. "
        "What is the most likely diagnosis? "
        "Provide 2-3 possible conditions and a brief medical explanation."
    )
    
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=200,
            temperature=0.7,
            top_p=0.9,
            do_sample=True
        )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Clean any repeated or trailing content
    return response.strip().split("\n")[0]


