from langchain_ollama import OllamaLLM

model = OllamaLLM(model="llama3.2", base_url="http://host.docker.internal:11434")