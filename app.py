import requests 
from flask import Flask, request
import os

app = Flask(__name__)

token = os.environ["TELEGRAM_BOT_TOKEN"]

# Conectando ao bot 
url = f"https://api.telegram.org/bot{token}/"

# Criando função que vai responder o usuário
def enviar_mensagem(chat_id, texto):
    url = url + "sendMessage"
    data = {"chat_id": chat_id, "text": texto}
    requests.post(url, json=data)

# Definindo as saídas de acordo com a escolha do usuário
def brasil():
    return "Você escolheu a opção 1"

def internacional():
    return "Você escolheu a opção 2"

def politica():
    return "Você escolheu a opção 3"

def economia():
    return "Você escolheu a opção 4"

# Criando a rota para manter o bot funcionando e criando menu com as opções
@app.route("/telegram", methods=["POST"])
def telegram_update():
    update = request.json
    url_envio_mensagem = f"https://api.telegram.org/bot{token}/sendMessage"
    chat_id = update["message"]["chat"]["id"]
    mensagem = {"chat_id": chat_id, "text": "mensagem <b>recebida</b>!", "parse_mode": "HTML"}
    requests.post(url_envio_mensagem, data=mensagem)
    return "ok"

if __name__ == '__main__':
    app.run(threaded=True)
