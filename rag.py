from dotenv import load_dotenv
from groq import Groq

from config import RAG_PROMPT_PATH, LLM_MODEL_NAME, TOP_K
from vectordb import VectorDB
from moderator import Moderator


class RAG:
    def __init__(self):
        load_dotenv()
        self.client = Groq()
        self.db = VectorDB()
        self.db.build_index()
        self.moderator = Moderator(self.client)

    def build_context(self, chunks):
        context = []
        for i, chunk in enumerate(chunks, start=1):
            context.append(
                f"[Chunk {i}]\n"
                f"Source: {chunk['metadata']}\n"
                f"Texte: {chunk['text']}"
            )
        return "\n\n".join(context)

    def answer_question(self, question: str) -> str:
        moderation = self.moderator.moderate(question)

        if moderation.get("is_prompt_injection") is True:
            return "Requête refusée : tentative de prompt injection détectée."

        chunks = self.db.retrieve(question, TOP_K)
        context = self.build_context(chunks)

        system_prompt = RAG_PROMPT_PATH.read_text(encoding="utf-8")
        system_prompt = system_prompt.replace("{{Chunks}}", context)

        response = self.client.chat.completions.create(
            model=LLM_MODEL_NAME,
            temperature=0.1,
            max_tokens=500,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question},
            ],
        )

        return response.choices[0].message.content