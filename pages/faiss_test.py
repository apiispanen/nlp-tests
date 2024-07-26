# pip install faiss-cpu
import faiss
# pip install sentence-transformers
from sentence_transformers import SentenceTransformer

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

# Example usage
texts = ["Hello world", "FAISS is great for similarity search", "Embeddings are useful for NLP tasks"]
embed_text_with_faiss(texts)
