from flask import Flask, request, jsonify
from werkzeug.middleware.proxy_fix import ProxyFix
from connections.ollama_connection import model

app = Flask(__name__)
app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

@app.route("/")
def hello():
    prompt = model.invoke("Come up with 10 names for a song about parrots")
    return prompt

@app.route('/prompt', methods=['POST'])
def handle_data():
    data = request.get_json()
    prompt = model.invoke(data["message"])

    # Return a response
    return jsonify({'response': prompt}), 200

if __name__ == "__main__":
    app.run()  # For development only