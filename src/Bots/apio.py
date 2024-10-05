from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("medalpaca/medalpaca-7b", use_fast=False)
model = AutoModelForCausalLM.from_pretrained("medalpaca/medalpaca-7b", torch_dtype=torch.float16)

# Move model to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Set the pad_token_id explicitly
model.config.pad_token_id = tokenizer.eos_token_id  # Typically, this is set to the EOS token

def chat_with_bot():
    print("Chatbot is ready! Type 'exit' to quit.")

    while True:
        # Get user input
        user_input = input("You: ")
        
        # Exit condition
        if user_input.lower() in ["exit", "quit"]:
            break

        # Tokenize the input
        inputs = tokenizer(user_input, return_tensors="pt").to(device)

        # Generate a response using the model
        output = model.generate(inputs['input_ids'], max_length=100, do_sample=True)

        # Decode the response back to text
        response = tokenizer.decode(output[0], skip_special_tokens=True)

        # Print the response
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat_with_bot()