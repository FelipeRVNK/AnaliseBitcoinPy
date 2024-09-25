import pandas as pd

# Caminho absoluto para o arquivo
file_path = r'C:\Users\hefen\PycharmProjects\pythonProject\Bitcoin.xlsx'

# Carregar o arquivo Excel
xls = pd.ExcelFile(file_path)

# Carregar a planilha "Dados"
df_dados = pd.read_excel(xls, sheet_name='Dados')

# Somar os valores das colunas 'Open' e 'Close'
soma_open = df_dados['Open'].sum()
soma_close = df_dados['Close'].sum()

# Contar valores válidos em ambas as colunas
contagem_open = df_dados['Open'].count()
contagem_close = df_dados['Close'].count()
total_valores = contagem_open + contagem_close

# Calcular a soma total e a média
soma_total = soma_open + soma_close
media_total = soma_total / total_valores

# Combinar os dados das duas colunas para calcular o desvio padrão
dados_combinados = pd.concat([df_dados['Open'], df_dados['Close']])

# Calcular o desvio padrão do conjunto combinado
desvio_padrao_comb = dados_combinados.std()

# Exibir os resultados
print("Soma dos valores na coluna 'Open':", soma_open)
print("Soma dos valores na coluna 'Close':", soma_close)
print("Contagem total de valores válidos:", total_valores)
print("Média calculada:", media_total)
print("Desvio padrão combinado das colunas 'Open' e 'Close':", desvio_padrao_comb)
