from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
import torch

app = Flask(__name__)
app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

@app.route("/")
def hello():
    if torch.cuda.is_available():
        return "GPU is available"
    else:
        return "GPU is not available"

if __name__ == "__main__":
    app.run()  # For development only