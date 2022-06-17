'''
                                             ####    CRIA FUNCAO pega_cotacao_moedas    ####
'''

def pega_cotacao_moedas(dicionario_moedas):                        
    import yfinance as yf                                        
            
    dicionario_cotacoes_moedas = {}                             # Cria o dicionário em que as moedas e suas respectivas cotações serão armazenadas
    for moeda in dicionario_moedas.keys():                        
        if moeda == "BRL":                                      # Cria uma verificação se a moeda é o Real
            dicionario_cotacoes_moedas["BRL"] = 1.00            # Atribui a cotação do Real para o próprio Real que é igual a 1
        else:                                           
            moeda_comparada_BRL = f"{moeda}BRL=X"               # Adapta para o padrão que a yfinance reconhece para buscar a cotação da moeda   
            try:                                                  
                cotacao = yf.Ticker(moeda_comparada_BRL).info["regularMarketPrice"]  # Acessa o histórico da moeda atrelada ao Real
                dicionario_cotacoes_moedas[moeda]= round(cotacao,2)
            except:                                                           
                try:
                    cotacao = yf.Ticker(f"{moeda}BRX=X").info["regularMarketPrice"]
                    dicionario_cotacoes_moedas[moeda]= round(cotacao,2)        # Adiciona a moeda e sua cotação ao dicionario_cotacoes_moedas
                except:
                    print("Cotação não encontrada")  
                            
    return dicionario_cotacoes_moedas                                          # Retorna o dicionario das moedas e cotações


'''
                                             ####    CRIA FUNCAO pega_preco_acoes    ####
'''

def pega_preco_acoes(dicionario_acoes):           
    import yfinance as yf                         
    dicionario_preco_acoes = {}                           # Cria o dicionário em que as ações e seus respectivos preços atuais serão armazenados
    for chave in dicionario_acoes.keys():         
        valor = yf.Ticker(chave).info.get('currentPrice') # Acessa o valor atual da ação 
        if valor == None:                                 # Cria uma condição que adapta para o padrão de nome das ações no yfinance
            chave_corrigida = f"{chave}.SA"
            try:    
                valor = yf.Ticker(chave_corrigida).info.get('currentPrice')  
                valor = round(valor,2)
            except:
                try:
                    valor = yf.Ticker(chave).info.get('regularMarketPrice')     # Segunda tentativa de encontrar o preço da ação
                    valor = round(valor,2)
                except:
                    try:
                        valor = yf.Ticker(chave_corrigida).info.get('regularMarketPrice')
                    except:
                        print(f"Valor da ação {chave} não encontrado")
                        dicionario_preco_acoes[chave] = "Não encontrado"
                
            dicionario_preco_acoes[chave] = valor   # Adiciona a ação e seu preço atual ao dicionario_preco_acoes
        else:
            valor = round(valor,2)
            dicionario_preco_acoes[chave] = valor   
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
            valor = round(valor,2)
            dicionario_preco_acoes_em_BRL[chave] = valor   
        else:
            if valor == None:                          
                chave_corrigida = f"{chave}.SA"    
                valor = yf.Ticker(chave_corrigida).info.get('currentPrice')
                
                if valor == None:
                    try:
                        valor = yf.Ticker(chave).info.get('regularMarketPrice')
                        print(valor)
                        valor = round(valor,2)
                        if valor != None:
                            dicionario_preco_acoes_em_BRL[chave] = valor
                            dic_moeda_difer_real = {currency_da_acao: chave}
                            dict_cotacao_real = pega_cotacao_moedas(dic_moeda_difer_real)
                            for cotacao_real in dict_cotacao_real.values():
                                preco_acao_convertido_BRL = cotacao_real * valor
                                dicionario_preco_acoes_em_BRL[chave] = round(preco_acao_convertido_BRL, 2) 
                        else:
                            print(f"Valor da ação {chave} não encontrado")
                            dicionario_preco_acoes_em_BRL[chave] = "Não encontrado" 
                    except:
                        print(f"Valor da ação {chave} não encontrado")
                        dicionario_preco_acoes_em_BRL[chave] = "Não encontrado"                
                else:
                    dicionario_preco_acoes_em_BRL[chave] = valor
                    dic_moeda_difer_real = {currency_da_acao: chave}
                    dict_cotacao_real = pega_cotacao_moedas(dic_moeda_difer_real)
                    for cotacao_real in dict_cotacao_real.values():
                        preco_acao_convertido_BRL = cotacao_real * valor
                        dicionario_preco_acoes_em_BRL[chave] = round(preco_acao_convertido_BRL, 2)
            else:       
                dic_moeda_difer_real = {currency_da_acao: chave}
                dict_cotacao_real = pega_cotacao_moedas(dic_moeda_difer_real)
                for cotacao_real in dict_cotacao_real.values():
                    preco_acao_convertido_BRL = cotacao_real * valor
                    dicionario_preco_acoes_em_BRL[chave] = round(preco_acao_convertido_BRL, 2)
    return dicionario_preco_acoes_em_BRL




'''
                                             ####    CRIA FUNCAO historico_acoes    ####
'''

def historico_moedas(dicionario_moedas):
    import yfinance as yf
    dicionario_historico_cotacoes_moedas = {}
    for moeda in dicionario_moedas.keys():                        
            if moeda == "BRL":                                    # Cria uma verificação se a moeda é o Real
                print("Não é possível obter histórico de uma moeda em relação à ela mesma")             
            else:                                                    
                moeda_comparada_BRL = f"{moeda}BRL=X"     # Adapta para o padrão que a yfinance reconhece para buscar o histórico atrelado ao Real.
                valor = yf.Ticker(moeda_comparada_BRL).history(period = "5y") # Acessa o histórico dos últimos 5 anos da moeda atrelada ao Real
                historico_cotacoes_moedas = valor[['Close']].copy()      #Cria um dataframe somente com as cotações passadas
                historico_cotacoes_moedas = historico_cotacoes_moedas.rename(columns = {'Close':'Cotação'})  #Altera o nome da coluna 

                if 'Empty' in str(valor):       #Verifica se o par de moedas possui histórico no yfinance
                    print(f"Não é possível pegar o histórico de {moeda} pareado ao Real(BRL) devido a inexistência no Yahoo Finance")
                else:
                    dicionario_historico_cotacoes_moedas[moeda]= historico_cotacoes_moedas # Insere no dicionario_historico_cotacoes_moedas o nome da moeda como chave e o histórico como valor.

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
    return dicionario_historico_preco_acoes


                                        ### FUNÇÕES DE APOIO ###
def apoio1(): # Função com o bloco try except da pega_preco_acao_em_BRL
    try:
        valor = yf.Ticker(chave).info.get('regularMarketPrice')
        print(valor)
        valor = round(valor,2)
        if valor != None:
            dicionario_preco_acoes_em_BRL[chave] = valor
            dic_moeda_difer_real = {currency_da_acao: chave}
            dict_cotacao_real = pega_cotacao_moedas(dic_moeda_difer_real)
            for cotacao_real in dict_cotacao_real.values():
                preco_acao_convertido_BRL = cotacao_real * valor
                dicionario_preco_acoes_em_BRL[chave] = round(preco_acao_convertido_BRL, 2) 
        else:
            print(f"Valor da ação {chave} não encontrado")
            dicionario_preco_acoes_em_BRL[chave] = "Não encontrado" 
    except:
        print(f"Valor da ação {chave} não encontrado")
        dicionario_preco_acoes_em_BRL[chave] = "Não encontrado"

def apoio2(): ## Converte o valor de uma ação estrangeira para real
    dic_moeda_difer_real = {currency_da_acao: chave}
    dict_cotacao_real = pega_cotacao_moedas(dic_moeda_difer_real)
    for cotacao_real in dict_cotacao_real.values():
        preco_acao_convertido_BRL = cotacao_real * valor
        dicionario_preco_acoes_em_BRL[chave] = round(preco_acao_convertido_BRL, 2)