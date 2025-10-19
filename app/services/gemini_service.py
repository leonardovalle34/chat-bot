import google.generativeai as genai
import os
import logging

logger = logging.getLogger(__name__)


class GeminiService:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.model = None
        if self.api_key:
            self.model = self._setup_gemini()

    def _setup_gemini(self):
        if not self.api_key:
            return None

        genai.configure(api_key=self.api_key)

        model_options = [
            'models/gemini-2.0-flash-001',
            'models/gemini-2.5-flash',
            'models/gemini-2.0-flash-lite-001',
        ]

        for model_name in model_options:
            try:
                logger.info(f"🔄 Tentando modelo: {model_name}")
                model = genai.GenerativeModel(model_name)
                # Teste rápido
                response = model.generate_content("Test")
                logger.info(f"✅ Modelo selecionado: {model_name}")
                return model
            except Exception as e:
                logger.warning(
                    f"❌ Modelo {model_name} falhou: {str(e)[:100]}...")
                continue

        return None

    def get_response(self, message):
        if not self.model:
            raise ValueError(
                "Gemini não configurado. Verifique a GEMINI_API_KEY.")

        response = self.model.generate_content(message)
        return response.text
