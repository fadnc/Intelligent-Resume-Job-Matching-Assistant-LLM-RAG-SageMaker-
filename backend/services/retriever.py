import faiss
import numpy as np
from config import FAISS_PATH, META_PATH

def create_index(vectors, chunks):
    dim = vectors.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(vectors)
    
    faiss.write_index(index, FAISS_PATH)
    np.save(META_PATH, np.array(chunks, dtype=object))
    
def search(query_vec, k=5):
    index = faiss.read_index(FAISS_PATH)
    chunks = np.load(META_PATH, allow_pickle=True)
    
    distances, indices = index.search(np.array([query_vec]), k)
    
    return [chunks[i] for i in indices[0]]