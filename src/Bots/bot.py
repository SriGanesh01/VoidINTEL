import fitz  # PyMuPDF for extracting PDF content
import ollama
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Function to extract text from PDFs
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

# Load the text from your PDF about medical myths
pdf_text = extract_text_from_pdf("path/to/your/medical_myths.pdf")

# Function to check if the question is about medical myths
def is_medical_myth_question(question):
    keywords = ["myth", "medicine", "health", "medical", "fact", "disease", "cure"]
    return any(keyword in question.lower() for keyword in keywords)

# Ask the Mistral model with medical myth filter
def ask_mistral_medical_myths(question, pdf_text):
    if is_medical_myth_question(question):
        question_with_context = f"From the following data: {pdf_text}, Answer this: {question}"
        response = ollama.ask("mistral", question_with_context)
        return response['text']
    else:
        return "I'm sorry, I can only answer questions related to medical myths."

# API Route for handling chatbot queries
@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json.get("question")
    response = ask_mistral_medical_myths(user_input, pdf_text)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
