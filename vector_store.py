from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

# use embedding model (NOT deepseek)
embedding = OllamaEmbeddings(model="nomic-embed-text")

# create database
db = Chroma(
    persist_directory="email_memory",
    embedding_function=embedding
)

def save_email(email):

    db.add_texts([email])

def search_email(query):

    results = db.similarity_search(query, k=1)

    if results:
        return results[0].page_content

    return "No email found"