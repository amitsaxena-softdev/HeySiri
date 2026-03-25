from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    app_name: str = "HeySiri"
    host: str = os.getenv("HEY_SIRI_HOST", "127.0.0.1")
    port: int = int(os.getenv("HEY_SIRI_PORT", "8000"))
    debug: bool = os.getenv("HEY_SIRI_DEBUG", "false").lower() == "true"
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    openai_model: str = os.getenv("HEY_SIRI_OPENAI_MODEL", "gpt-4o-mini")


settings = Settings()
