import openpyxl
from openpyxl.utils import get_column_letter


def dados(ws, ativo, cota, col):

    linha = 2
    for nome in ativo.keys():
        quant = ativo[nome]
        cotacao = quant * cota[nome]

        ws.cell(column=col, row=linha, value=nome)
        ws.cell(column=col+1, row=linha, value=quant)
        ws.cell(column=col+2, row=linha, value=cotacao).number_format = 'R$#,##0.00'

        linha += 1
    return ws


def redimensionar(ws):

    dims = {}
    for row in ws.rows:
        for cell in row:
            if cell.value:
                dims[cell.column_letter] = max((dims.get(cell.column_letter, 0), len(str(cell.value))))
    for col, value in dims.items():
        ws.column_dimensions[col].width = value + 10
    return ws


def planilha(moedas, acoes, moedas_cota, acoes_cota):

    wb = openpyxl.Workbook()

    ws1 = wb.active
    ws1.title = "Carteira"

    ws1.append(["Moedas", "Quantidade", "Cotação", "", "Ações", "Quantidade", "Cotação"])

    ws1 = dados(ws1, moedas, moedas_cota, 1)
    ws1 = dados(ws1, acoes, acoes_cota, 5)

    # Redimensionando as celas
    ws1 = redimensionar(ws1)

    dest_filename = input("Digite o nome  de arquivo: ")+'.xlsx'
    wb.save(filename=dest_filename)
