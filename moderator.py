import json
from groq import Groq
from config import MODERATOR_PROMPT_PATH, LLM_MODEL_NAME


class Moderator:
    def __init__(self, client: Groq):
        self.client = client
        self.system_prompt = MODERATOR_PROMPT_PATH.read_text(encoding="utf-8")

    def moderate(self, question: str) -> dict:
        response = self.client.chat.completions.create(
            model=LLM_MODEL_NAME,
            temperature=0,
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": question},
            ],
        )
        return json.loads(response.choices[0].message.content)