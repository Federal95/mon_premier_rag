from pathlib import Path

# Racine du projet
BASE_DIR = Path(__file__).resolve().parent

# Chemins du projet
DATA_DIR = BASE_DIR / "data"
PROMPTS_DIR = BASE_DIR / "prompts"
CHROMA_DIR = BASE_DIR / "chroma_db"

CSV_PATH = DATA_DIR / "05_chunking_rag.csv"

RAG_PROMPT_PATH = PROMPTS_DIR / "rag_system.txt"
MODERATOR_PROMPT_PATH = PROMPTS_DIR / "moderator.txt"

# Modèles
EMBEDDING_MODEL_NAME = "distiluse-base-multilingual-cased-v2"
LLM_MODEL_NAME = "llama-3.3-70b-versatile"

# ChromaDB
COLLECTION_NAME = "rag_chunks"

# Retrieval
TOP_K = 3