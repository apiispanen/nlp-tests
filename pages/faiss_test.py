# pip install faiss-cpu
import faiss
# pip install sentence-transformers
from sentence_transformers import SentenceTransformer

import streamlit as st


def embed_text_with_faiss(text_list):
    # Load a pre-trained sentence transformer model
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Generate embeddings for the text list
    embeddings = model.encode(text_list)
    
    # Create a FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    
    # Add embeddings to the index
    index.add(embeddings)
    
    # Print the embeddings
    print("Embeddings:\n", embeddings)
    return index, embeddings


def similarity_search(text, embeddings, index):
    # Load a pre-trained sentence transformer model
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Generate embeddings for the text
    query_embedding = model.encode([text])
    
    # Search for similar embeddings
    k = 5
    D, I = index.search(query_embedding, k)
    
    # Print the similar embeddings
    print("Similar embeddings:\n", embeddings[I[0]])
    return embeddings[I[0]]


text_area = st.text_area("Enter text")

if st.button("Embed text"):
    text_list = text_area.split("\n")
    index, embeddings = embed_text_with_faiss(text_list)
    st.write(embeddings)
    st.write("Text embedded successfully")


if st.button("Search similar text"):
    text = st.text_input("Enter text to search")
    similarity_search(text, embeddings, index)
    st.write("Text searched successfully")