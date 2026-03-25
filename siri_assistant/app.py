from __future__ import annotations

from flask import Flask

from siri_assistant.api.routes import register_api
from siri_assistant.core.command_processor import CommandProcessor
from siri_assistant.logging_config import configure_logging
from siri_assistant.services.llm_service import build_llm_service
from siri_assistant.web.routes import web_bp


def create_app() -> Flask:
    configure_logging()

    app = Flask(__name__, template_folder="web/templates", static_folder="web/static")

    processor = CommandProcessor(build_llm_service())
    app.register_blueprint(register_api(processor))
    app.register_blueprint(web_bp)

    return app
