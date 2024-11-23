from flask import Flask, request, jsonify
from werkzeug.middleware.proxy_fix import ProxyFix
from connections.ollama_connection import model
from routes.simple_page import simple_page

app = Flask(__name__)
app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

@app.route("/")
def hello():
    if torch.cuda.is_available():
        return "GPU is available"
    else:
        return "GPU not available"

@app.route('/prompt', methods=['POST'])
def handle_data():
    data = request.get_json()
    prompt = model.invoke(data["message"])
    return jsonify({'response': prompt}), 200

app.register_blueprint(simple_page)

if __name__ == "__main__":
    app.run()
