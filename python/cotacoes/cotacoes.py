def pega_cotacao_moedas(dicionario_moedas):                        # PRÉ REQUISITO para usar essa função: existir um dicionário com nome          dicionario_moedas(para passar como parâmetro para a função) com o padrão {--MOEDA-- : --QUANTIDADE--}
    import yfinance as yf                                         # Importa o yfinance
            
    dicionario_cotacoes_moedas = {}                               # Cria o dicionário em que as moedas e suas respectivas cotações serão armazenadas
    for moeda in dicionario_moedas.keys():                        # Cria um loop que percorre as chaves(no caso, as moedas/"currencies") do  dicionário((criado a partir do scrapping do HTML) das moedas e da quantidade que o cliente possui delas
        if moeda == "BRL": # Cria uma verificação se a moeda é o Real, para que não haja problemas ao buscar a cotação na biblioteca yfinance
            dicionario_cotacoes_moedas["BRL"] = 1.00              # Atribui a cotação do Real para o próprio Real que é igual a 1
        else:                                                     # Caso não seja a moeda Real o código abaixo será executado
            moeda_comparada_BRL = f"{moeda}BRL=X"                 # Adapta para o padrão que a yfinance reconhece para buscar a cotação da moeda   atrelada ao Real.
            try:                                                  # Verifica se a cotação atrelada ao real será encontrada, e em caso positivo o seguinte código é executado:
                valor = yf.Ticker(moeda_comparada_BRL).history()  # Acessa o histórico da moeda atrelada ao Real
                cotacao = valor.at[valor.index[-1],"Close"]       # Busca a cotação mais recente da moeda(pelo preço de fechamento em tempo real quando o mercado financeiro esá ativo, ou o último preço fechado quando não está ativo, que é o da cotação atual.)
                dicionario_cotacoes_moedas[moeda]= round(cotacao,2)        # Adiciona a moeda e sua cotação ao dicionario_cotacoes_moedas
            except IndexError:                                    # Caso o par de moedas não seja encontrado na biblioteca, imprime que a cotação não foi encontrada.
                print("Cotação não encontrada")                
    print(dicionario_cotacoes_moedas)                             # Imprime o dicionario das moedas e cotações
    return dicionario_cotacoes_moedas                             # Retorna o dicionario das moedas e cotações



def pega_preco_acoes(dicionario_acoes):
    import yfinance as yf
    dicionario_preco_acoes = {}
    for chave in dicionario_acoes.keys():
        valor = yf.Ticker(chave).info.get('currentPrice')
        if valor == None:
            chave_corrigida = f"{chave}.SA"
            valor = yf.Ticker(chave_corrigida).info.get('currentPrice')
            valor = round(valor,2)
            dicionario_preco_acoes[chave] = valor
        else:
            valor = round(valor,2)
            dicionario_preco_acoes[chave] = valor

    print(dicionario_preco_acoes)
    return dicionario_preco_acoes
