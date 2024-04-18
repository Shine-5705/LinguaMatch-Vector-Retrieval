# LinguaMatch-Vector-Retrieval
A system that retrieves relevant documents in one language based on a query in another language, using vectorization techniques for semantic search.
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1 align="center">Semantic Search</h1>

<p>Welcome to Semantic Search, a powerful tool for searching through text documents using natural language queries.</p>

<h2>Features</h2>

<ul>
  <li><strong>Translation:</strong> Translate queries from English to French seamlessly using Google Translate API.</li>
  <li><strong>Semantic Search:</strong> Perform semantic search on a corpus of French documents.</li>
  <li><strong>Interactive GUI:</strong> User-friendly GUI interface for ease of use.</li>
</ul>

<h2>Installation</h2>

<ol>
  <li>Clone the repository:</li>
  <code>git clone https://github.com/Shine-5705/LinguaMatch-Vector-Retrieval.git</code>
  <li>Navigate to the project directory:</li>
  <code>cd semantic-search</code>
  <li>Install the required packages:</li>
  <code>pip install -r requirements.txt</code>
</ol>

<h2>Usage</h2>

<ol>
  <li>Run the <code>semantic_search_gui.py</code> script:</li>
  <code>python semantic_search_gui.py</code>
  <li>Enter your query in English and click on the "Search" button. Relevant French documents along with their similarity scores will be displayed.</li>
</ol>

<h2>Example</h2>

<pre><code>query = "a quick fox jumps over a lazy dog"
translated_query = translate_query(query, source_lang='en', target_lang='fr')
similarities, relevant_document_indices = semantic_search(query, translated_query, french_matrix, top_n=3)

print("Query (English):", query)
print("Translated Query (French):", translated_query)
print("\nRelevant Documents (French):")
for idx in relevant_document_indices:
    print("- Document:", french_documents[idx])
    print("  Similarity Score:", similarities[0][idx])
    print()
</code></pre>

<h2>Screenshots</h2>

<div align="center">
  <img src="https://yourrepository.com/semantic-search-gui.png" alt="Semantic Search GUI">
</div>

<h2>Credits</h2>

<p>This project uses the <code>googletrans</code> library for translation.</p>

<h2>License</h2>

<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

</body>
</html>
