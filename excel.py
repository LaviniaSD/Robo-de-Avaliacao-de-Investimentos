
def valor_total(moedas, acoes, moedas_cota, acoes_cota):
    soma=0
    for moeda, quant_moeda in moedas.items():
        soma  += quant_moeda * moedas_cota[moeda]
        
    for acao, quant_acao in acoes.items():
        soma += quant_acao * acoes_cota[acao]
    return soma
