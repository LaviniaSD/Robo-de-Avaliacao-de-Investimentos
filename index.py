#Importe os módulos necessários e suas funções
from pacote_a2_ic import scraping
from pacote_a2_ic import cotacoes
from pacote_a2_ic import excel
from pacote_a2_ic import graficos_historicos
from pacote_a2_ic.scraping import *
from pacote_a2_ic.cotacoes import *
from pacote_a2_ic.excel import *
from pacote_a2_ic.graficos_historicos import *

#Cria variáveis para os retornos das funções do módulo scraping

sentinela = 0
while sentinela != -1:
    try:
        html_lido = scraping.pegue_site()
        dicionario_moedas = scraping.dic_moedas(html_lido)
        dicionario_acoes = scraping.dic_acoes(html_lido)

        #Pegue no yahoo finance informações sobre as moedas e ações lidas e coloque-as em variáveis

        dicionario_cotacoes_moedas = cotacoes.pega_cotacao_moedas(dicionario_moedas)
        dicionario_preco_acoes = cotacoes.pega_preco_acoes(dicionario_acoes)
        dicionario_historico_cotacoes_moedas = cotacoes.historico_moedas(dicionario_cotacoes_moedas)
        dicionario_historico_preco_acoes = cotacoes.historico_acoes(dicionario_preco_acoes)
        dicionario_preco_acoes_em_BRL = cotacoes.pega_preco_acao_em_BRL(dicionario_preco_acoes)


        #Cria a planilha com os dados da carteira
        excel.planilha(dicionario_moedas, dicionario_acoes, dicionario_cotacoes_moedas, dicionario_preco_acoes_em_BRL)

        #Adicione os gráficos à planilha
        graficos_historicos.graficos_acoes(dicionario_historico_preco_acoes)
        graficos_historicos.graficos_moedas(dicionario_historico_cotacoes_moedas)

        #Calcule o valor total e adicione o qrcode
        valor_total=excel.valor_total(dicionario_moedas, dicionario_acoes, dicionario_cotacoes_moedas, dicionario_preco_acoes_em_BRL)
        excel.qr(valor_total)
        sentinela = -1
    except:
        sentinela = 0
        
        

