#Bibliotecas necessárias
from urllib.request import urlopen
from bs4 import BeautifulSoup

#Função que pede url e pega seu html
def pegue_site():
    url = input("Insira aqui sua url: ")
    html = urlopen(url)
    html_lido= BeautifulSoup(html, 'html.parser')
    return html_lido
    
#transforma o valor retornado da função pegue_site em uma variável
#html_lido = pegue_site()

#Pega a tabela na div de classe 'moeda' do html e retorna um dicionário com as moedas e suas quantidades 
def dic_moedas(hipertext):
    div_moeda = hipertext.find_all("div", {"class": "moeda"})
    for moeda in div_moeda:
        linhas_moeda = moeda.find_all('tr')
    dicionario_moedas = {}
    for linha in linhas_moeda:
        children = linha.findChildren("td")
        if children == []:
            children == []
        else:
            dicionario_moedas[children[0].text] = int(children[1].text)
    return dicionario_moedas

#Pega a tabela na div de classe 'acao' do html e retorna um dicionário com as ações e suas quantidades 
def dic_acoes(hipertext):
    div_acoes = hipertext.find_all("div", {"class": "acao"})
    for acao in div_acoes:
        linhas_acoes = acao.find_all('tr')
    dicionario_acoes = {}
    for linha in linhas_acoes:
        children = linha.findChildren("td")
        if children == []:
            children == []
        else:
            dicionario_acoes[children[0].text] = int(children[1].text)
    return dicionario_acoes
