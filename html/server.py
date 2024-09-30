from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Configure Google AI API
genai.configure(api_key="AIzaSyC-aiJVFc7lXEvvEjZopG7yo7ZgGarWiH4")

# Create the model
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "max_output_tokens": 2048,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    generation_config=generation_config,
)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message')

    # AI Chat response
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(user_message)
    
    return jsonify({"response": response.text})

if __name__ == '__main__':
    app.run(debug=True)
