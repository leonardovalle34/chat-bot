from flask import Blueprint, request, jsonify
import logging
from app.services.gemini_service import GeminiService

logger = logging.getLogger(__name__)
chat_bp = Blueprint("chat", __name__)


gemini_service = GeminiService()


@chat_bp.route(
    "/chat", methods=["POST"]
)  # route for chat interactions
def chat():
    try:
        data = request.json

        if not data:
            return (
                jsonify(
                    {"error": "No input data provided"}
                ),
                400,
            )

        user_message = data.get("message", "").strip()

        if not user_message:
            return (
                jsonify({"error": "Message is required"}),
                400,
            )

        logger.info(f"💬 Mensagem recebida: {user_message}")

        bot_response = gemini_service.get_response(
            user_message
        )

        logger.info(f"✅ Resposta gerada com sucesso")

        return (
            jsonify(
                {
                    "response": bot_response,
                    "status": "success",
                    "model": "gemini",
                }
            ),
            200,
        )

    except Exception as e:
        logger.error(f"❌ Erro no chat: {e}")
        return jsonify({"error": str(e)}), 500


@chat_bp.route(
    "/test", methods=["GET"]
)  # test route for Gemini integration
def test_gemini():
    try:
        test_prompt = "Hello, how are you? Respond briefly in one sentence."

        response = gemini_service.get_response(test_prompt)

        return (
            jsonify(
                {
                    "test_prompt": test_prompt,
                    "response": response,
                    "status": "success",
                    "model": "gemini",
                }
            ),
            200,
        )

    except Exception as e:
        logger.error(f"❌ Erro no teste: {e}")
        return jsonify({"error": str(e)}), 500
