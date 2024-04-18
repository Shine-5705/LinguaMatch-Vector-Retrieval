import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from googletrans import Translator

# Load English and French data
def load_data(path):
    with open(path, "r", encoding="utf-8") as f:
        data = f.read()
    return data.split('\n')

english_documents = load_data('english')
french_documents = load_data('french')

# Preprocess and Vectorize
vectorizer = TfidfVectorizer(stop_words='english')
english_matrix = vectorizer.fit_transform(english_documents).toarray()
french_matrix = vectorizer.fit_transform(french_documents).toarray()

# Translate Query
def translate_query(query, source_lang='en', target_lang='fr'):
    translator = Translator()
    translated_query = translator.translate(query, src=source_lang, dest=target_lang)
    return translated_query.text

# Semantic Search
def semantic_search(query, translated_query, french_matrix, top_n=5):
    query_vector = vectorizer.transform([translated_query]).toarray()
    similarities = cosine_similarity(query_vector, french_matrix)
    ranked_indices = np.argsort(similarities[0])[::-1][:top_n]
    return similarities, ranked_indices

def search_query():
    query = query_entry.get()
    if not query:
        messagebox.showerror("Error", "Please enter a query.")
        return
    
    translated_query = translate_query(query, source_lang='en', target_lang='fr')
    similarities, relevant_document_indices = semantic_search(query, translated_query, french_matrix, top_n=3)
    
    result_text.config(state=tk.NORMAL)
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, "Query (English): " + query + "\n")
    result_text.insert(tk.END, "Translated Query (French): " + translated_query + "\n\n")
    result_text.insert(tk.END, "Relevant Documents (French):\n")
    for idx in relevant_document_indices:
        result_text.insert(tk.END, "- Document: " + french_documents[idx] + "\n")
        result_text.insert(tk.END, "  Similarity Score: " + str(similarities[0][idx]) + "\n\n")
    result_text.config(state=tk.DISABLED)

# Create tkinter GUI
root = tk.Tk()
root.title("Semantic Search")
root.geometry("600x400")

# Query Entry
query_label = tk.Label(root, text="Enter Query (English):")
query_label.pack(pady=10)

query_entry = tk.Entry(root, width=50)
query_entry.pack()

# Search Button
search_button = tk.Button(root, text="Search", command=search_query)
search_button.pack(pady=10)

# Result Text
result_text = scrolledtext.ScrolledText(root, width=60, height=20, wrap=tk.WORD)
result_text.pack(pady=10)
result_text.insert(tk.END, "Search results will appear here.")

result_text.config(state=tk.DISABLED)

root.mainloop()
