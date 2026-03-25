from __future__ import annotations

import datetime
from dataclasses import dataclass

from siri_assistant.services.llm_service import LLMService


@dataclass
class CommandResult:
    text: str
    action: str = "speak"
    url: str | None = None


class CommandProcessor:
    def __init__(self, llm_service: LLMService) -> None:
        self.llm_service = llm_service
        self.sites = {
            "youtube": "https://youtube.com",
            "wikipedia": "https://wikipedia.com",
            "udemy": "https://udemy.com",
            "facebook": "https://facebook.com",
            "instagram": "https://instagram.com",
            "google": "https://google.com",
        }

    def process(self, query: str) -> CommandResult:
        normalized = query.lower().strip()

        if not normalized:
            return CommandResult(text="I didn't hear anything. Please try again.")

        if any(word in normalized for word in ["stop", "exit", "end", "bye", "see you"]):
            return CommandResult(text="Okay, talk to you later.", action="stop")

        if "time" in normalized:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            return CommandResult(text=f"The time is {now}.")

        for name, url in self.sites.items():
            if name in normalized:
                return CommandResult(text=f"Opening {name}.", action="open_url", url=url)

        answer = self.llm_service.ask(query)
        return CommandResult(text=answer)
