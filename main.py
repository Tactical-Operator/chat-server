from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

messages = []


@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    messages.append(data)
    return jsonify({"status": "Message received"}), 200


@app.route('/receive', methods=['GET'])
def get_messages():
    return jsonify(messages), 200


@app.route('/clear', methods=['POST'])
def clear_messages():
    messages.clear()
    return jsonify({"status": "Messages cleared"}), 200


app.run(host='0.0.0.0', port=8080)
