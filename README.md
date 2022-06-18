<h1>Robô de avaliação de investimentos</h1>
> Status: Concluído

<h3>Índice:</h3>
=================

   * [Sobre o projeto](#sobre)
   * [Pré Requisitos](#pre-requisitos)
   * [Como ler esse projeto?](#como-ler)
   * [Nossa Equipe](#equipe)



<h3 id=sobre>Sobre o projeto:</h3>

Este projeto tem como objetivo ler uma página web que contenha uma carteira financeira com moedas e ações e suas respectivas quantidades e levar essas informações para uma planilha excel.

  A planilha conterá cada ativo, sua quantidade e o valor total que o proprietário da carteira possui em reais. Além disso, a planilha conterá gráficos referentes ao histórico de cotação de alguns ativos e um Qrcode com o valor total que o proprietário possui em reais na carteira disponibilizada.

<h3 id=pre-requisitos>Pré requisitos:</h3>

1. Possuir uma URL que contenha uma tabela apenas com as ações dentro da tag :
```
<div class='acao'> 
```
e que contenha outra tabela só com as moedas dentro da tag:
```
<div class='moeda'> 
```
2. Os nomes das ações devem estar de acordo com seus nomes no [YahooFinance](https://finance.yahoo.com/)
  
⚠️ Atenção: Ativos escritos incorretamente não serão tratados e contabilizados


<h3 id=como-ler>Como ler esse projeto?</h3>
Para entender e executar esse projeto siga as seguintes instruções:
  
- [ ] Instale em seu computador a biblioteca BeautifulSoup do Python
  
```
pip install beautifulsoup4
```

- [ ] Instale em seu computador a biblioteca urllib3
  
```
pip install urllib3
``` 
- [ ] Instale a biblioteca Openpyxl do Python
  
```
pip install openpyxl
```
  
- [ ] Instale a biblioteca Yfinance do Python
  
```
pip install yfinance
```
  
- [ ] Instale a biblioteca qrcode do Python
  
```
pip install qrcode
```

- [ ] Instale a biblioteca qrcode do Python
  
```
pip install pandas
```

- [ ] Instale a biblioteca qrcode do Python
  
```
pip install datetime
```

- [ ] Instale a biblioteca qrcode do Python
  
```
pip install os
```

- [ ] Instale a biblioteca qrcode do Python
  
```
pip install glob
```


- [ ] Instale os módulos principal.py, excel.py,webscraping.py,financas.py
- [ ] Coloque todos os módulos na mesma pasta de seu computador
- [ ] Execute o módulo principal.py
- [ ] insira uma URL que atenda aos [pré-requisitos](#pre-requisitos),caso não tenha uma, utilize nossas carteiras teste:
  * [Carteira 1](https://laviniasd.github.io/Robo-de-Avaliacao-de-Investimentos/index.html)
  * [Carteira 2](https://laviniasd.github.io/Robo-de-Avaliacao-de-Investimentos/site2/pagina2.html)
  * [Carteira 3](https://laviniasd.github.io/Robo-de-Avaliacao-de-Investimentos/site3/pagina3.html)
  
 Observação: Caso queira ver o html e css utilizado em cada carteira, vá em sua  respectiva pasta nesse repositório.
  
  <h3 id=equipe>Nossa equipe:</h3>
  
  * [Luan Carvalho](https://github.com/Luan-vht3)
  
  * [Yonathan Rabinovici](https://github.com/yonirg)
   
  * [George Vaz](https://github.com/GeorgeRV)
   
  * [Lavínia Dias](https://github.com/LaviniaSD)
  
  * Téo Braga
