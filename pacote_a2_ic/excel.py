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


#bibliotecas necessárias
import openpyxl as opx
import qrcode

#Função que lê os dicionários de moedas e ações e suas cotações e retorna o total (em reais) da carteira.
def valor_total(moedas, acoes, moedas_cota, acoes_cota):
    soma=0
    for moeda, quant_moeda in moedas.items():
        soma  += quant_moeda * moedas_cota[moeda]
        
    for acao, quant_acao in acoes.items():
        soma += quant_acao * acoes_cota[acao]
    return soma

#Função que insere um qrcode com o valor total da carteira na planilha excel da mesma.
def qr(soma):
    wb = opx.load_workbook(filename="carteira.xlsx")
    ws = wb.create_sheet(title="QrCode")
    qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_H,box_size = 10, border = 4)
    qr.add_data(soma)
    img=qr.make_image()
    img.save('total.png')
    img = opx.drawing.image.Image('total.png')
    ws.add_image(img, "A1")
    wb.save(filename="carteira.xlsx")



