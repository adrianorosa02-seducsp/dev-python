from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Projeto Inetz Online!</h1><p>Rodando via Poetry em um container isolado.</p>"

if __name__ == "__main__":
    # Importante: host='0.0.0.0' para ser acessível fora do container
    app.run(host='0.0.0.0', port=5000)