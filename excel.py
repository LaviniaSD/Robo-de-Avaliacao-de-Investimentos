import openpyxl

def planilha(moedas, acoes, moedas_cota, acoes_cota):
    wb = openpyxl.Workbook()

    ws1 = wb.active
    ws1.title = "Carteira"


    ws1.append(["Moedas", "Quantidade", "Cotação"])


    for moeda, quant_moeda in moedas.items():
        #print('moeda', moeda, "qmoeda",quant_moeda)
        cota  = quant_moeda * moedas_cota[moeda]
        linha = (moeda, quant_moeda, cota)
        ws1.append(linha)
        
    ws1.append([""])
    ws1.append(["Ações", "Quantidade", "Cotação"])

    for acao, quant_acao in acoes.items():
        #print('acao',acao, "quant_acao",quant_acao)
        cota  = quant_acao * acoes_cota[acao]
        linha = (acao, quant_acao, cota)
        ws1.append(linha)

    dest_filename = input("Digite o nome  de arquivo: ")+ '.xlsx'
    wb.save(filename = dest_filename)


