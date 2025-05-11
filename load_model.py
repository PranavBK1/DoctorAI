from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load BioGPT model from Hugging Face
model_name = "microsoft/BioGPT"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def ask_ai(symptoms: str) -> str:
    prompt = (
        f"Given the symptoms: {symptoms}. "
        "What is the most likely diagnosis? "
        "Provide 2-3 possible conditions with a brief medical explanation for each."
    )

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    input_ids = inputs["input_ids"]

    with torch.no_grad():
        output_ids = model.generate(
            input_ids,
            max_length=512,
            temperature=0.7,
            top_p=0.9,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )

    decoded_output = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    # Remove the prompt if it echoes it
    if decoded_output.startswith(prompt):
        decoded_output = decoded_output[len(prompt):].strip()

    return decoded_output.strip()



