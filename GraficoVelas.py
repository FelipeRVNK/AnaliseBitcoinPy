import pandas as pd
import mplfinance as mpf


file_path = r'C:\Users\hefen\PycharmProjects\pythonProject\Bitcoin.xlsx'


df_dados = pd.read_excel(file_path, sheet_name='Dados')


df_dados['Date'] = pd.to_datetime(df_dados['Date'])


df_dados.set_index('Date', inplace=True)


mpf.plot(df_dados, type='candle', style='charles', volume=False, title='Gráfico de Velas: Bitcoin', ylabel='Preço', figsize=(12, 6))
