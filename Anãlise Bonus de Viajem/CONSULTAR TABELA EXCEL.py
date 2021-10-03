import pandas as pd
from twilio.rest import Client


account_sid = "ACf891c038fd236ffe7ac36a97a9e560f1"
auth_token = "c07271671198a102db9b400e952c8272"
client = Client(account_sid, auth_token)

# pip install pandas
# pip install openpyxl
# pip install twilio

# Abrir os arquivos em excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    # print(mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    # print(tabela_vendas)
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes} {vendedor} bateu a meta de R$55 000,00 com R${vendas} em vendas')
        message = client.messages.create(
            to="+5521987051148",
            from_="+13093966472",
            body=f'No mês de {mes} {vendedor} bateu a meta de R$55 000,00 com R${vendas} em vendas')
        print(message.sid)
