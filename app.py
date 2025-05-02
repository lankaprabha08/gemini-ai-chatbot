from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app, resources={r"/chat": {"origins": "http://127.0.0.1:5500"}})

GEMINI_API_KEY = "your_actual_api_key_here"
genai.configure(api_key=GEMINI_API_KEY)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message")

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(user_input)

    reply = response.text if hasattr(response, "text") else "No response from Gemini AI."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(port=5000)
