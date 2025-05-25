from flask import Flask, render_template, request, jsonify
from chatbot.chatbot_engine import get_medical_response
import webbrowser
import threading
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    response = get_medical_response(user_input)
    return jsonify({"response": response})

@app.route('/shutdown', methods=['POST'])
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        return "Not running with the Werkzeug Server", 500
    func()
    return "Server shutting down..."

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == '__main__':
    threading.Timer(1.5, open_browser).start()
    app.run(debug=True, use_reloader=False)
