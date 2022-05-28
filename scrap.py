#Bibliotecas necessárias
from urllib.request import urlopen
from bs4 import BeautifulSoup

#Função que pede url e pega seu html
def pegue_site():
    url = input("Insira aqui sua url: ")
    html = urlopen(url)
    html_lido= BeautifulSoup(html, 'html.parser')
    return comandos_lido
    
