from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

def load_vector_store():
    return FAISS.load_local("vector_db", OpenAIEmbeddings())

def retrieve_examples(query):
    db = load_vector_store()
    return db.similarity_search(query, k=3)