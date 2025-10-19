from flask import Flask  # Flask creates server
from flask_cors import CORS  # CORS handles Cross-Origin Resource Sharing
import os  # Operating system interactions
from dotenv import load_dotenv  # Load environment variables from .env file

load_dotenv()


def create_app():
    app = Flask(__name__)
    CORS(app)

    # Register blueprints/routes
    from app.routes.chat import chat_bp
    from app.routes.health import health_bp

    app.register_blueprint(chat_bp)
    app.register_blueprint(health_bp)

    return app
