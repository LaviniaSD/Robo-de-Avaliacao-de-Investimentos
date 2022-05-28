'''
                                             ####    CRIA FUNCAO pega_cotacao_moedas    ####
'''

def pega_cotacao_moedas(dicionario_moedas):                        # PRÉ REQUISITO/SUGESTÃO para usar essa função: existir um dicionário com nome dicionario_moedas <----[SUGESTÃO] (para passar como parâmetro para a função) com o padrão {--MOEDA-- : --QUANTIDADE--}  <----[PRÉ REQUISITO]
    import yfinance as yf                                         # Importa o yfinance
            
    dicionario_cotacoes_moedas = {}                               # Cria o dicionário em que as moedas e suas respectivas cotações serão armazenadas
    for moeda in dicionario_moedas.keys():                        # Cria um loop que percorre as chaves(no caso, as moedas/"currencies") do  dicionário(criado a partir do scrapping do HTML) das moedas e da quantidade que o cliente possui delas
        if moeda == "BRL": # Cria uma verificação se a moeda é o Real, para que não haja problemas ao buscar a cotação na biblioteca yfinance
            dicionario_cotacoes_moedas["BRL"] = 1.00              # Atribui a cotação do Real para o próprio Real que é igual a 1
        elif moeda == "USD":    
            moeda_comparada_BRL = "BRL=X"
            try:                                                  # Verifica se a cotação atrelada ao real será encontrada, e em caso positivo o seguinte código é executado:
                valor = yf.Ticker(moeda_comparada_BRL).history()  # Acessa o histórico da moeda atrelada ao Real
                cotacao = valor.at[valor.index[-1],"Close"]       # Busca a cotação mais recente da moeda(pelo preço de fechamento em tempo real quando o mercado financeiro esá ativo, ou o último preço fechado quando não está ativo, que é o da cotação atual.)
                dicionario_cotacoes_moedas[moeda]= round(cotacao,2)
            except:
                                                                  # Adiciona a moeda e sua cotação ao dicionario_cotacoes_moedas
                try:
                    valor = yf.Ticker(f"{moeda}BRX=X").history()
                    cotacao = valor.at[valor.index[-1],"Close"]
                    dicionario_cotacoes_moedas[moeda]= round(cotacao,2)
                except IndexError:                                    # Caso o par de moedas não seja encontrado na biblioteca, imprime que a cotação não foi encontrada.
                    print("Cotação não encontrada")  
                except:
                    print("Algo deu errado, tente novamente")  
        else:                                           # Caso não seja a moeda Real o código abaixo será executado
            moeda_comparada_BRL = f"{moeda}BRL=X"                 # Adapta para o padrão que a yfinance reconhece para buscar a cotação da moeda   atrelada ao Real.
            try:                                                  # Verifica se a cotação atrelada ao real será encontrada, e em caso positivo o seguinte código é executado:
                valor = yf.Ticker(moeda_comparada_BRL).history()  # Acessa o histórico da moeda atrelada ao Real
                cotacao = valor.at[valor.index[-1],"Close"]       # Busca a cotação mais recente da moeda(pelo preço de fechamento em tempo real quando o mercado financeiro esá ativo, ou o último preço fechado quando não está ativo, que é o da cotação atual.)
                dicionario_cotacoes_moedas[moeda]= round(cotacao,2)
            except:
                #print("Algo de errado ocorreu, tente novamente")        # Adiciona a moeda e sua cotação ao dicionario_cotacoes_moedas
                try:
                    valor = yf.Ticker(f"{moeda}BRX=X").history()
                    cotacao = valor.at[valor.index[-1],"Close"]
                    dicionario_cotacoes_moedas[moeda]= round(cotacao,2)
                except IndexError:                                    # Caso o par de moedas não seja encontrado na biblioteca, imprime que a cotação não foi encontrada.
                    print("Cotação não encontrada")  
                except:
                    print("Algo deu errado, tente novamente")  
                            
    print(dicionario_cotacoes_moedas)                             # Imprime o dicionario das moedas e cotações
    return dicionario_cotacoes_moedas                             # Retorna o dicionario das moedas e cotações


'''
                                             ####    CRIA FUNCAO pega_preco_acoes    ####
'''

def pega_preco_acoes(dicionario_acoes):           # PRÉ REQUISITO/SUGESTÃO para usar essa função: existir um dicionário com nome dicionario_acoes <----[SUGESTÃO](para passar como parâmetro para a função) com o padrão {--CÓDIGO DA AÇÃO-- : --QUANTIDADE--}   <----[PRÉ REQUISITO]
    import yfinance as yf                         # Importa o yfinance
    dicionario_preco_acoes = {}                   # Cria o dicionário em que as ações e seus respectivos preços atuais serão armazenados
    for chave in dicionario_acoes.keys():         # Cria um loop que percorre as chaves(no caso, as ações) do  dicionário(criado a partir do scrapping do HTML) das ações e da quantidade que o cliente possui delas
        valor = yf.Ticker(chave).info.get('currentPrice')       # Acessa o valor atual da ação 
        if valor == None:                         # Cria uma condição que adapta para o padrão de nome das ações no yfinance(Exemplo: nome_da_ação.SA) caso não encontre somente com o código da ação.
            chave_corrigida = f"{chave}.SA"    
            valor = yf.Ticker(chave_corrigida).info.get('currentPrice')
            valor = round(valor,2)                
            dicionario_preco_acoes[chave] = valor   # Adiciona a ação e seu preço atual ao dicionario_preco_acoes
        else:
            valor = round(valor,2)
            dicionario_preco_acoes[chave] = valor   # Adiciona a ação e seu preço atual ao dicionario_preco_acoes

    print(dicionario_preco_acoes)                   # Imprime o dicionario das ações e seus preços
    return dicionario_preco_acoes                   # Retorna o dicionario das ações e seus preços na moeda local

'''
                                        ####    CRIA FUNCAO pega_preco_acao_em_BRL   ####
'''

def pega_preco_acao_em_BRL(dicionario_acoes):
    import yfinance as yf                         
    dicionario_preco_acoes_em_BRL = {}                   
    for chave in dicionario_acoes.keys():         
        valor = yf.Ticker(chave).info.get('currentPrice')        
        currency_da_acao = yf.Ticker(chave).info.get('currency')
        if currency_da_acao == "BRL":
            if valor == None:                          
                chave_corrigida = f"{chave}.SA"    
                valor = yf.Ticker(chave_corrigida).info.get('currentPrice')
                valor = round(valor,2)                
                dicionario_preco_acoes_em_BRL[chave] = valor   
            else:
                valor = round(valor,2)
                dicionario_preco_acoes_em_BRL[chave] = valor   
        else:
            dic_moeda_difer_real = {currency_da_acao: chave}
            dict_cotacao_real = pega_cotacao_moedas(dic_moeda_difer_real)
            for cotacao_real in dict_cotacao_real.values():
                pass 
            preco_acao_convertido_BRL = cotacao_real * valor
            dicionario_preco_acoes_em_BRL[chave] = round(preco_acao_convertido_BRL, 2)
    print(dicionario_preco_acoes_em_BRL)
    return dicionario_preco_acoes_em_BRL




'''
                                             ####    CRIA FUNCAO historico_acoes    ####
'''

def historico_moedas(dicionario_moedas):
    import yfinance as yf
    dicionario_historico_cotacoes_moedas = {}
    for moeda in dicionario_moedas.keys():                        # Cria um loop que percorre as chaves(no caso, as moedas/"currencies") do  dicionário(criado a partir do scrapping do HTML) das moedas e da quantidade que o cliente possui delas
            if moeda == "BRL":                                    # Cria uma verificação se a moeda é o Real, para que não haja problemas ao buscar o histórico na biblioteca yfinance
                print("Não é possível obter histórico de uma moeda em relação à ela mesma")             
            else:                                                     # Caso não seja a moeda Real o código abaixo será executado
                moeda_comparada_BRL = f"{moeda}BRL=X"                 # Adapta para o padrão que a yfinance reconhece para buscar o histórico atrelado ao Real.
                valor = yf.Ticker(moeda_comparada_BRL).history(period = "5y")     # Acessa o histórico dos últimos 5 anos da moeda atrelada ao Real
                historico_cotacoes_moedas = valor[['Close']].copy()      #Cria um dataframe somente com a data e coluna Close a partir do extraído da biblioteca
                historico_cotacoes_moedas = historico_cotacoes_moedas.rename(columns = {'Close':'Cotação'})     #Altera o nome da coluna desse DataFrame para cotação

                if 'Empty' in str(valor):       #Verifica se o par de moedas possui histórico no Yahoo Finanance, como nos casos MOEDABRX=X que não existe.
                    print(f"Não é possível pegar o histórico de {moeda} pareado ao Real(BRL) devido a inexistência no Yahoo Finance")
                else:
                    dicionario_historico_cotacoes_moedas[moeda]= historico_cotacoes_moedas # Insere no dicionario_historico_cotacoes_moedas o nome da moeda como chave e o histórico como valor.

    print(dicionario_historico_cotacoes_moedas) # Imprime o dicionario das ações e seus preços
    return dicionario_historico_cotacoes_moedas # Retorna o dicionario das ações e seus preços



def historico_acoes(dicionario_acoes):
    import yfinance as yf
    dicionario_historico_preco_acoes = {}
    for acao in dicionario_acoes.keys():
        historico_acao = yf.Ticker(acao).history(period = "5y")
        if "Empty" in str(historico_acao):
            historico_acao = yf.Ticker(f"{acao}.SA").history(period = "5y")
            if "Empty" in str(historico_acao):
                print("Ação não encontrada no yahoo Finance")
                dicionario_historico_preco_acoes[acao] = "Ação não encontrada" 
            else:
                historico_preco_acao = historico_acao[["Close"]].copy()
                historico_preco_acao = historico_preco_acao.rename(columns = {"Close": "Preço"})
                dicionario_historico_preco_acoes[acao] = historico_preco_acao
        
        else:  
            historico_preco_acao = historico_acao[["Close"]].copy()
            historico_preco_acao = historico_preco_acao.rename(columns = {"Close": "Preço"})
            dicionario_historico_preco_acoes[acao] = historico_preco_acao
    print(dicionario_historico_preco_acoes)
    return dicionario_historico_preco_acoes




