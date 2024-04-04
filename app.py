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
@app.route('/telegram', methods=['POST'])
def mensagem():
    mensagem = request.json
    chat_id = mensagem['message']['chat']['id']
    texto = mensagem['message']['text']
    
    if texto == '/start':
        resposta = "Escolha uma opção:\n1. Brasil\n2. Internacional\n3. Política\n4. Economia"
    elif texto == '1':
        resposta = brasil()
    elif texto == '2':
        resposta = internacional()
    elif texto == '3':
        resposta = politica()
    elif texto == '4':
        resposta = economia()
    else:
        resposta = "Opção inválida. Por favor, escolha um dos quatro temas."

    enviar_mensagem(chat_id, resposta)
    return "OK", 200

if __name__ == '__main__':
    app.run(threaded=True)
