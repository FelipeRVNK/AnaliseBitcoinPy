import pandas as pd
import matplotlib.pyplot as plt


file_path = r'C:\Users\hefen\PycharmProjects\pythonProject\Bitcoin.xlsx'

df_dados = pd.read_excel(file_path, sheet_name='Dados')


df_dados['Date'] = pd.to_datetime(df_dados['Date'])


plt.figure(figsize=(12, 6))
plt.plot(df_dados['Date'], df_dados['Volume'], label='Volume', color='blue')
plt.xlabel('Data')
plt.ylabel('Volume')
plt.title('Gráfico de Linhas entre Data e Volume')
plt.legend()
plt.grid()
plt.show()
