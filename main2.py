import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from googletrans import Translator

def load_data(path):
    with open(path,"r",encoding="utf-8") as f:
        data=f.read()
    return data.split('\n')

english_documents=load_data('english')
french_documents=load_data('french')

vectorizer=TfidfVectorizer(stop_words='english')
english_matrix=vectorizer.fit_transform(english_documents).toarray()
french_matrix=vectorizer.fit_transform(french_documents).toarray()

def translate_query(query, source_lang='en', target_lang='fr'):
    translator = Translator()
    translated_query = translator.translate(query, src=source_lang, dest=target_lang)
    return translated_query.text

def semantic_search(query, translated_query, french_matrix, top_n=5):
    query_vector = vectorizer.transform([translated_query]).toarray()
    similarities = cosine_similarity(query_vector, french_matrix)
    ranked_indices = np.argsort(similarities[0])[::-1][:top_n]
    return similarities, ranked_indices

query = "a quick fox jum over a lazy dog"
translated_query = translate_query(query, source_lang='en', target_lang='fr')
similarities, relevant_document_indices = semantic_search(query, translated_query, french_matrix, top_n=3)
print("Query (English):", query)
print("Translated Query (French):", translated_query)
print("\nRelevant Documents (French):")
for idx in relevant_document_indices:
    print("- Document:", french_documents[idx])
    print("  Similarity Score:", similarities[0][idx])
    print()
