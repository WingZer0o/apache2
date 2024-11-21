from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
from langchain_ollama import OllamaLLM

app = Flask(__name__)
app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

@app.route("/")
def hello():
    model = OllamaLLM(model="llama3.1", base_url="http://host.docker.internal:11434")
    prompt = model.invoke("Come up with 10 names for a song about parrots")
    return prompt


if __name__ == "__main__":
    app.run()  # For development only