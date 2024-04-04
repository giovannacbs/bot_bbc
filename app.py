import requests 
from flask import Flask, request
import os
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

token = os.environ["TELEGRAM_BOT_TOKEN"]

# Conectando ao bot 
url = f"https://api.telegram.org/bot{token}/"

# Criando função que vai responder o usuário
def enviar_mensagem(chat_id, texto):
    url_mensagem = url + "sendMessage"
    data = {"chat_id": chat_id, "text": texto}
    requests.post(url_mensagem, json=data)

# Definindo as saídas de acordo com a escolha do usuário
def brasil():
    tema = 'cz74k717pw5t'  
    noticias = exibir_top5(tema)
    resposta = "Últimas notícias sobre o Brasil:\n"
    for titulo, link in noticias:
        resposta += f"{titulo}\nLink: https://www.bbc.com{link}\n\n"
    return resposta

def internacional():
    tema = 'cmdm4ynm24kt'  
    noticias = exibir_top5(tema)
    resposta = "Últimas notícias internacionais:\n"
    for titulo, link in noticias:
        resposta += f"{titulo}\nLink: https://www.bbc.com{link}\n\n"
    return resposta

def tecnologia():
    tema = 'c404v027pd4t'  
    noticias = exibir_top5(tema)
    resposta = "Últimas notícias sobre tecnologia:\n"
    for titulo, link in noticias:
        resposta += f"{titulo}\nLink: https://www.bbc.com{link}\n\n"
    return resposta

def economia():
    tema = 'cmdm4ynm24kt'  
    noticias = exibir_top5(tema)
    resposta = "Últimas notícias de Economia:\n"
    for titulo, link in noticias:
        resposta += f"{titulo}\nLink: https://www.bbc.com{link}\n\n"
    return resposta


# Criando a rota para manter o bot funcionando e criando menu com as opções
@app.route('/mensagem', methods=['POST'])
def mensagem():
    mensagem = request.json
    chat_id = mensagem['message']['chat']['id']
    texto = mensagem['message']['text']
    
    if texto == '/start':
        resposta = "Escolha uma opção e responda com o número selecionado:\n1. Brasil\n2. Internacional\n3. Política\n4. Economia"
    elif texto == '1':
        resposta = brasil()
    elif texto == '2':
        resposta = internacional()
    elif texto == '3':
        resposta = tecnologia()
    elif texto == '4':
        resposta = economia()
    else:
        resposta = "Opção inválida. Por favor, escolha um dos quatro temas."

    enviar_mensagem(chat_id, resposta)
    return "OK", 200

if __name__ == '__main__':
    app.run(threaded=True)

def exibir_top5(tema):
  url = 'https://www.bbc.com/portuguese/topics/' + tema

  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')

  h2 = soup.find_all('h2') # look for all titles 
  titulos = []
  for h in h2:
    titulo = h.get_text()
    titulos.append(titulo)

  titulos = titulos[:5] # select only first 5
  
  links = soup.find_all('a', {'class' : 'focusIndicatorDisplayBlock bbc-uk8dsi e1d658bg0'})
  
  hrefs = []
  for href in links:
    hrefs.append(href.get('href'))

  hrefs = hrefs[:5]

  materias = list(zip(titulos, hrefs))

  return materias