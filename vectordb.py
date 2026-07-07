import pandas as pd
import chromadb
from sentence_transformers import SentenceTransformer

from config import (
    CSV_PATH,
    CHROMA_DIR,
    COLLECTION_NAME,
    EMBEDDING_MODEL_NAME,
)


class VectorDB:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=str(CHROMA_DIR))
        self.embedding_model = SentenceTransformer(EMBEDDING_MODEL_NAME)

        self.collection = self.client.get_or_create_collection(
            name=COLLECTION_NAME,
            metadata={"embedding_model": EMBEDDING_MODEL_NAME},
        )

    def load_chunks_from_csv(self):
        df = pd.read_csv(CSV_PATH)

        if "chunk" in df.columns:
            text_column = "chunk"
        elif "text" in df.columns:
            text_column = "text"
        elif "content" in df.columns:
            text_column = "content"
        else:
            text_column = df.columns[0]

        chunks = []
        for index, row in df.iterrows():
            text = str(row[text_column]).strip()
            if text:
                chunks.append(
                    {
                        "id": f"chunk_{index}",
                        "text": text,
                        "metadata": {
                            "source": "05_chunking_rag.csv",
                            "row": int(index),
                        },
                    }
                )

        return chunks

    def encode(self, texts):
        return self.embedding_model.encode(
            texts,
            normalize_embeddings=True,
            show_progress_bar=True,
        ).tolist()

    def build_index(self):
        if self.collection.count() > 0:
            print("Base ChromaDB déjà existante : pas de réindexation.")
            return

        chunks = self.load_chunks_from_csv()
        documents = [chunk["text"] for chunk in chunks]
        ids = [chunk["id"] for chunk in chunks]
        metadatas = [chunk["metadata"] for chunk in chunks]

        embeddings = self.encode(documents)

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
        )

        print(f"{len(chunks)} chunks indexés dans ChromaDB.")

    def retrieve(self, question, n_results=3):
        question_embedding = self.encode([question])[0]

        results = self.collection.query(
            query_embeddings=[question_embedding],
            n_results=n_results,
            include=["documents", "metadatas", "distances"],
        )

        retrieved_chunks = []

        for doc, metadata, distance in zip(
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0],
        ):
            retrieved_chunks.append(
                {
                    "text": doc,
                    "metadata": metadata,
                    "distance": distance,
                }
            )

        return retrieved_chunks