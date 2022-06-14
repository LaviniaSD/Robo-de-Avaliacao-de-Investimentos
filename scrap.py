#bibliotecas necessárias para o web scraping
from urllib.request import urlopen
from bs4 import BeautifulSoup


def pegue_site(): # Lê a url inserida pelo usuário e retorna o html do site
    url = input("Insira aqui sua url: ")
    try:
        html = urlopen(url)
        html_lido= BeautifulSoup(html, 'html.parser')
    except : 
        print('Esse não é um site, tente novamente.')
    else:
        return html_lido






def dic_moedas(hipertext): #Acha no html a classe moeda e retorna um dicionário com as informações que estão em uma tabela dentro da classe
    try:
        div_moeda = hipertext.find_all("div", {"class": "moeda"})
        for moeda in div_moeda:
            linhas_moeda = moeda.find_all('tr')
        dicionario_moedas = {}
        for linha in linhas_moeda:
            children = linha.findChildren("td")
            if children == []:
                children == []
            else:
                dicionario_moedas[children[0].text] = float(children[1].text)
    except:
        print('Não foi possível achar moedas nessa carteira')
    else:
        return dicionario_moedas
    
    

def dic_acoes(hipertext):#Acha no html a classe 'acao' e retorna um dicionário com as informações que estão em uma tabela dentro da classe
    try:
        div_acoes = hipertext.find_all("div", {"class": "acao"})
        for acao in div_acoes:
            linhas_acoes = acao.find_all('tr')
        dicionario_acoes = {}
        for linha in linhas_acoes:
            children = linha.findChildren("td")
            if children == []:
                children == []
            else:
                dicionario_acoes[children[0].text] = float(children[1].text)
    except:
        print('Não foi possível achar ações nessa carteira')
    else:
        return dicionario_acoes
