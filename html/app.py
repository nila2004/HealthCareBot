# app.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Placeholder for storing chat messages
chat_history = []

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.json.get('message')  # Use .get() to avoid KeyError
    if message:
        chat_history.append({'sender': 'user', 'message': message})
        
        # Example response from the server (bot-like response)
        reply = f"You said: {message}"
        chat_history.append({'sender': 'bot', 'message': reply})
    
    return jsonify(chat_history)  # Always return a JSON response

if __name__ == '__main__':
    app.run(debug=True)
