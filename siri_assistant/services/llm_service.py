from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Protocol

from siri_assistant.config import settings

logger = logging.getLogger(__name__)

try:
    from openai import OpenAI
except Exception:  # pragma: no cover
    OpenAI = None


class LLMService(Protocol):
    def ask(self, query: str) -> str:
        ...


@dataclass
class OpenAIService:
    model: str
    api_key: str

    def ask(self, query: str) -> str:
        if not self.api_key:
            return "OPENAI_API_KEY is not configured. Add it to your environment to enable AI chat."

        if OpenAI is None:
            return "OpenAI client is unavailable. Install dependencies from requirements.txt."

        try:
            client = OpenAI(api_key=self.api_key)
            response = client.responses.create(
                model=self.model,
                input=[
                    {
                        "role": "system",
                        "content": "You are HeySiri, a concise and helpful voice assistant.",
                    },
                    {"role": "user", "content": query},
                ],
            )
            return response.output_text.strip()
        except Exception as exc:
            logger.exception("Failed to call OpenAI", exc_info=exc)
            return "I hit an error while calling the AI service. Please try again."


def build_llm_service() -> LLMService:
    return OpenAIService(model=settings.openai_model, api_key=settings.openai_api_key)
