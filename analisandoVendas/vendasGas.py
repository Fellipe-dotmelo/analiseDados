import pandas as pd
import matplotlib.pyplot as plt

# Abra o arquivo Excel com todas as abas
xlsx = pd.ExcelFile('melhorGas_analise.xlsx.xlsx')

# Escolha a aba que deseja plotar (substitua 'Dia 02' pelo nome da aba desejada)
sheet_name = 'Dia 02'

# Leia os dados da aba escolhida
df = pd.read_excel(xlsx, sheet_name)

# Plotar os dados como um gráfico de barras
plt.figure(figsize=(10, 6))  # Ajuste o tamanho do gráfico conforme necessário
plt.bar(df['Unnamed: 0'], df['Unnamed: 1'])  # Use 'Item' como rótulo do eixo X
plt.title('Gráfico de Barras')
plt.xticks(rotation=45)  # Rotação dos rótulos do eixo X, se necessário
plt.show()

# Feche o arquivo Excel
xlsx.close()
