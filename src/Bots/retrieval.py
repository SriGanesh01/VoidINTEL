
import numpy as np
from sentence_transformers import SentenceTransformer
from pdf_reader import extract_text_from_pdf

PDF_PATH = "aguaistapious1.pdf" 

document_text = extract_text_from_pdf(PDF_PATH)

model = SentenceTransformer('all-MiniLM-L6-v2') 

document_embedding = model.encode(document_text)

def get_embedding(query):
    """Get the embedding for the user query."""
    return model.encode(query)

def query_index(query_embedding):
    """Retrieve the most relevant document based on the query embedding."""
    similarity = np.dot(query_embedding, document_embedding)
    return document_text 

def retrieve_relevant_document(user_input):
    """Retrieve a relevant document based on user input."""
    query_embedding = get_embedding(user_input)
    return query_index(query_embedding) 
