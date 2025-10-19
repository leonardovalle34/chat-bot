from app import create_app
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = create_app()

if __name__ == '__main__':
    port = int(os.getenv("PORT", 8080))
    debug = os.getenv("FLASK_DEBUG", "true").lower() == "true"

    logger.info(f"🚀 Iniciando servidor na porta {port}")
    logger.info(f"🔑 Gemini configurado: {bool(os.getenv('GEMINI_API_KEY'))}")

    app.run(host='0.0.0.0', port=port, debug=debug)
