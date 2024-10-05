# server.py
import pdfplumber
from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to extract health myths from the PDF
def extract_myths_from_pdf(pdf_path):
    myths = {}
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            # Define extraction logic based on the structure of your PDF
            lines = text.split('\n')
            for i, line in enumerate(lines):
                if '?' in line:  # Assuming health-related myths end with "?"
                    question = line.strip().lower()
                    answer = lines[i + 1].strip() if i + 1 < len(lines) else "No answer available"
                    myths[question] = answer
    return myths

# Load myths from the PDF located in assets
myth_data = extract_myths_from_pdf('src/assets/aguaistapious1.pdf')

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()
    # Check if the message is in the health myth data
    response = myth_data.get(user_message, "I only know about health topics. Please ask a medical question.")
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(port=5000)
