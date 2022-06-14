import openpyxl as opx
import qrcode


def valor_total(moedas, acoes, moedas_cota, acoes_cota):
    soma=0
    for moeda, quant_moeda in moedas.items():
        soma  += quant_moeda * moedas_cota[moeda]
        
    for acao, quant_acao in acoes.items():
        soma += quant_acao * acoes_cota[acao]
    return soma

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
