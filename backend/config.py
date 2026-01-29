import os
from dotenv import load_dotenv

load_dotenv()

EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

USE_SAGEMAKER = False
SAGEMAKER_ENDPOINT = os.getenv("SAGEMAKER_ENDPOINT", "")

FAISS_PATH = "embeddings_store/faiss_index"
META_PATH = "embeddings_store/meta.npy"
