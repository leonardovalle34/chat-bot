
## 🚀 Quick Start

```bash
# Clone and setup
git clone https://github.com/YOUR_USERNAME/chatbot-flask.git
cd chatbot-flask/backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your Gemini API key

# Run the application
python run.py

📚 API Endpoints
GET / - API status

GET /health - Health check

POST /chat - Send message to chatbot

GET /test - Test Gemini integration

🛠️ Technologies
Python 3.10+

Flask

Google Gemini AI

Vue.js (frontend ready)
