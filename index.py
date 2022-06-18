from pacote_a2_ic import scraping
from pacote_a2_ic import cotacoes
from pacote_a2_ic import excel
from pacote_a2_ic import graficos_historicos
from pacote_a2_ic.scraping import *
from pacote_a2_ic.cotacoes import *
from pacote_a2_ic.excel import *
from pacote_a2_ic.graficos_historicos import *

html_lido = scraping.pegue_site()
dicionario_moedas = scraping.dic_moedas(html_lido)
dicionario_acoes = scraping.dic_acoes(html_lido)

dicionario_cotacoes_moedas = cotacoes.pega_cotacao_moedas(dicionario_moedas)
dicionario_preco_acoes = cotacoes.pega_preco_acoes(dicionario_acoes)
dicionario_historico_cotacoes_moedas = cotacoes.historico_moedas(dicionario_cotacoes_moedas)
dicionario_historico_preco_acoes = cotacoes.historico_acoes(dicionario_preco_acoes)
dicionario_preco_acoes_em_BRL = cotacoes.pega_preco_acao_em_BRL(dicionario_preco_acoes)
excel.planilha(dicionario_moedas, dicionario_acoes, dicionario_cotacoes_moedas, dicionario_preco_acoes_em_BRL)
graficos_historicos.graficos_acoes(dicionario_historico_preco_acoes)
graficos_historicos.graficos_moedas(dicionario_historico_cotacoes_moedas)
valor_total=excel.valor_total(dicionario_moedas, dicionario_acoes, dicionario_cotacoes_moedas, dicionario_preco_acoes_em_BRL)
excel.qr(valor_total)
