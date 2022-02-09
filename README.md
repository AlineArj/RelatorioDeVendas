# Relatorio De Vendas
![GitHub](https://img.shields.io/github/license/AlineArj/RelatorioDeVendas?color=red&style=for-the-badge)

Exercício para fins de estudo utilizando Pandas para análise de dados, elaboração e envio automático de relatório. 


## 📊 Sobre o projeto

O banco de dados analisado diz respeito a uma série de vendas feitas em alguns shoppings, aproximadamente 10.100 registros de compras. As informações registradas nele são: Data da compra, ID da Loja, Produto, Quantidade, Valor Unitário e Valor Total. 

Foi feita uma análise desses dados afim de se obter o Faturamento, Quantidade de Itens Vendidos e o Ticket Médio (média de preço por produto vendido) em cada shopping. Após isso, um relatório é gerado e enviado automaticamente para o e-mail desejado.

## 👾 Instalação

#### Bibliotecas Necessárias
- Pandas 
- OpenPyXl (biblioteca de apoio ao Pandas para leitura do arquivo em excel).
- Win32 (biblioteca para automação do envio de e-mails).

*OBS:* É necessário ter o Outlook instalado e configurado na sua máquina!

``` bach
$ python3
$ pip install pandas
$ pip install openpyxl
$ pip install pywin32h
$ main.py
```

*OBS2:* Lembre de alterar o e-mail de envio no código para um e-mail que você tenha acesso antes de roda-lo.

![email](https://github.com/AlineArj/RelatorioDeVendas/blob/main/Imagens/email.png)
