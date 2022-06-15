from pacote_a2_ic import scrap
from pacote_a2_ic import cotacoes
from pacote_a2_ic import excel
from pacote_a2_ic import graficos_historicos
from pacote_a2_ic.scrap import *
from pacote_a2_ic.cotacoes import *
from pacote_a2_ic.excel import *
from pacote_a2_ic.graficos_historicos import *

html_lido = scrap.pegue_site()
dicionario_moedas = scrap.dic_moedas(html_lido)
dicionario_acoes = scrap.dic_acoes(html_lido)
dicionario_cotacoes_moedas = cotacoes.pega_cotacao_moedas(dicionario_moedas)
dicionario_preco_acoes = cotacoes.pega_preco_acoes(dicionario_acoes)
dicionario_historico_cotacoes_moedas = cotacoes.historico_moedas(dicionario_cotacoes_moedas)
dicionario_historico_preco_acoes = cotacoes.historico_acoes(dicionario_preco_acoes)
dicionario_preco_acoes_em_BRL = cotacoes.pega_preco_acao_em_BRL(dicionario_preco_acoes)
planilha_criada = excel.planilha(dicionario_moedas, dicionario_acoes, dicionario_cotacoes_moedas, dicionario_preco_acoes_em_BRL)
grafico_acoes = graficos_historicos.cria_grafico_acoes(dicionario_historico_preco_acoes)
grafico_moedas = graficos_historicos.cria_grafico_moedas(dicionario_historico_cotacoes_moedas)
historico_moedas=cotacoes.historico_moedas(dicionario_moedas)
historico_acoes=cotacoes.historico_acoes(dicionario_acoes)
excel.planilha(dicionario_moedas, dicionario_acoes, dicionario_cotacoes_moedas, dicionario_preco_acoes_em_BRL)
graficos_historicos.graficos(historico_moedas,historico_acoes)
valor_total=excel.valor_total(dicionario_moedas, dicionario_acoes, cotacao_moedas, preco_acao_em_BRL)
excel.qrcode(valor_total)

