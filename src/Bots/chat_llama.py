import subprocess
from retrieval import retrieve_relevant_document

def chat_with_llama():
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        # Retrieve relevant document based on user input
        relevant_doc = retrieve_relevant_document(user_input)

        # Prepare the input for LLaMA, combining user input and the retrieved document
        combined_input = f"{relevant_doc}\nUser: {user_input}"

        # Run the LLaMA model with the combined input and stream the output
        process = subprocess.Popen(
            ["ollama", "run", "llama3.1"],  # Adjust the command as necessary
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Pass the input to the process
        process.stdin.write(combined_input)
        process.stdin.close()

        # Read the output word by word and print progressively
        while True:
            output = process.stdout.read(1)  # Read character by character
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output, end='', flush=True)  # Print without adding a newline, and flush the output

        # Check for errors
        if process.returncode != 0:
            error_message = process.stderr.read().strip()
            print(f"\nError: {error_message}")

if __name__ == "__main__":
    chat_with_llama()