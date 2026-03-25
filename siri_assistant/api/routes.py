from __future__ import annotations

from flask import Blueprint, jsonify, request

from siri_assistant.api.schemas import ChatRequest, ChatResponse
from siri_assistant.core.command_processor import CommandProcessor


api_bp = Blueprint("api", __name__, url_prefix="/api")


def register_api(processor: CommandProcessor) -> Blueprint:
    @api_bp.post("/chat")
    def chat() -> tuple:
        payload = request.get_json(force=True, silent=True) or {}
        data = ChatRequest.model_validate(payload)

        result = processor.process(data.query)
        response = ChatResponse(text=result.text, action=result.action, url=result.url)
        return jsonify(response.model_dump()), 200

    @api_bp.get("/health")
    def health() -> tuple:
        return jsonify({"status": "ok"}), 200

    return api_bp
