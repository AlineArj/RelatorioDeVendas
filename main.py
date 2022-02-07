import pandas as pd
import win32com.client as win32

# Visualização da tabela Vendas
tab_vendas = pd.read_excel('Vendas.xlsx')
pd.set_option('display.max_columns', None)
print(tab_vendas)

df = tab_vendas[['ID Loja','Valor Final', 'Quantidade']].groupby('ID Loja').sum()
df_media = (df['Valor Final'] / df['Quantidade']).to_frame()
df = df.join(df_media, on='ID Loja')

df = df.rename(columns={'Valor Final': 'Faturamento', 'Quantidade': 'Itens Vendidos', 0:'Ticket Médio'})

# Envio do relatório
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)

mail.To = 'alinearj@outlook.com.br'
mail.Subject = 'Relatório de Vendas'
mail.HTMLBody = f'''
<p>Prezados,</p>

<p>Segue o Relatório de Vendas por cada loja.</p>

{df.to_html(formatters={'Faturamento': 'R${:,.2f}'.format, 'Ticket Médio': 'R${:,.2f}'.format})}

<p>Qualquer dúvida estou à disposição.</p>

<p>Atenciosamente,</p>
<p>Aline Araujo</p>
'''

mail.Send()
print("E-mail enviado com sucesso")
