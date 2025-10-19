from flask import Blueprint, jsonify
import os
import logging

logger = logging.getLogger(__name__)
health_bp = Blueprint('health', __name__)


@health_bp.route('/')  # home route
def home():
    return jsonify(
        {
            "message": (
                "🚀 ChatBot Flask API está funcionando!"
            ),
            "status": "online",
            "gemini_configured": bool(
                os.getenv("GEMINI_API_KEY")
            ),
        }
    )


@health_bp.route(
    '/health', methods=['GET']
)  # health check route
def health_check():
    gemini_status = (
        "configured"
        if os.getenv("GEMINI_API_KEY")
        else "not configured"
    )
    return (
        jsonify(
            {"status": "healthy", "gemini": gemini_status}
        ),
        200,
    )
