import webbrowser
import time
from datetime import date
from datetime import datetime

#Datas
data_atual = date.today()

#hora
now = datetime.now()
x = now.hour
y = now.minute

nome = input('Nome do usúario: ')
id = int(input(f'{nome} digite a senha de acesso: '))

#tempo
import requests
API = 'e917f37910fa5b188d95588523e79a39'
cidade = input('Digite a cidade para saber a previsão do tempo: ')
site = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API}&lang=pt_br"
requisicao = requests.get(site)
requisicao_dic = requisicao.json()
previsao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] - 273.15
#random para escolha de músicas aleatorias
import random
musica2 = random.choice(['https://www.youtube.com/watch?v=1m7BoW5_J0k', 'https://www.youtube.com/watch?v=RqiRWIYMlnA', 'https://www.youtube.com/watch?v=Tw0_qHNRAEA',
                                                                                                             'https://www.youtube.com/watch?v=kE0unyetlBw'])





if id == 2323:
    print ('Irei te passar algumas informações do dia')
    print(f'{nome} são exatamente {x}horas e {y}minutos ')
    time.sleep(2)
    print(f'{nome} a data atual de hoje {data_atual}')
    time.sleep(2)
    print(previsao, f"previsão do tempo de hoje {temperatura:.2f}ºC")
    time.sleep(2)
    print(f'EMAIL importante para você {nome}, Nubank mandou um email informando que sua fatura irá fechar em breve.')
    time.sleep(3)

while id == 2323:
    ajuda = input('Precisa de mais alguma coisa? ')
    if ajuda == 'música':
        webbrowser.open('https://www.youtube.com/watch?v=UCskpE9KGQU')
    elif ajuda == 'tocar m. jackson':
        webbrowser.open('https://www.youtube.com/watch?v=h_D3VFfhvs4')
    elif ajuda == 'noticias':
        webbrowser.open('https://g1.globo.com/')
    elif ajuda == 'estou com fome':
        print('Irei abrir o APP do ifood')
        time.sleep(2)
        webbrowser.open('https://www.ifood.com.br/')



























































