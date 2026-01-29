def chunk_text(text, size=800, overlap=200):
    if overlap >= size:
        raise ValueError("Overlap must be smaller than size.")
        
    chunks = []
    start = 0
    
    while start < len(text):
        end = start + size
        chunks.append(text[start:end])
        start += size - overlap
    
    return chunks