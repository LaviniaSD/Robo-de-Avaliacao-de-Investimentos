import openpyxl as opx
import pandas as pd

wb = opx.Workbook()

### Histórico das moedas
def cria_grafico_moedas(dicionario_historico_cotacoes_moedas):
    ws_moedas = wb.active
    ws_moedas.title = "Histórico_moedas"

    ws_moedas["A1"] = "Histórico das moedas"
    # pd.from_dict()
    df_moedas = pd.DataFrame(dicionario_historico_cotacoes_moedas)

    dados_moedas = opx.chart.Reference(df_moedas) # Referencia o dataframe do histórico das moedas
    graf_hist_moedas = opx.chart.LineChart()
    graf_hist_moedas.add_data(dados_moedas)
    ws_moedas.add_chart(graf_hist_moedas, "F1") # Posição do gráfico


### Histórico das ações
def cria_grafico_acoes(dicionario_historico_preco_acoes):
    ws_acoes = wb.create_sheet(title="Histórico_ações")

    ws_acoes["A1"] = "Histórico das ações"
    df_acoes = pd.DataFrame(dicionario_historico_preco_acoes)

    dados_acoes = opx.chart.Reference(df_acoes) # Referencia o dataframe do histórico das ações
    graf_hist_acoes = opx.chart.LineChart()
    graf_hist_acoes.add_data(dados_acoes)
    ws_acoes.add_chart(graf_hist_acoes, "F1") # Posição do gráfico


    wb.save("Gráficos_do_Histórico.xlsx")
