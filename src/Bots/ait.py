import subprocess
import sys

def chat_with_llama():
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        response = subprocess.run(
            ["ollama", "run", "llama3.1"],
            input=user_input,
            text=True,
            capture_output=True,
            encoding='utf-8'
        )

        if response.returncode != 0:
            print("Error:", response.stderr.strip())
        else:
            print(f"LLaMA: {response.stdout.strip()}")

if __name__ == "__main__":
    chat_with_llama()
