import pandas as pd
import matplotlib.pyplot as plt

# Carregue o arquivo Excel com os dados
pessoas = pd.read_excel("pessoas.xlsx")

# Extraia a coluna 'Idade' do DataFrame
idades = pessoas['Idade']

# Crie um gráfico de pizza com base nas idades
plt.pie(idades, labels=pessoas['Nome'], autopct="%1.0f%%")  # Use 'Nome' para as etiquetas no gráfico
plt.show()
