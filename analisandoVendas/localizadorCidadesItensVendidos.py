from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import pandas as pd
import matplotlib.pyplot as plt

# Importar a planilha
vendasProdutos = 'vendas_dados atual.xlsx'

dias_do_mes = range(1, 31)
abas = [f'dia{dia}' for dia in dias_do_mes]

# Inicializar a lista para armazenar os DataFrames
dataframes = []

# Itere sobre as abas e leia cada uma delas, adicionando à lista apenas se a aba existir
for aba in abas:
    try:
        df_aba = pd.read_excel(vendasProdutos, sheet_name=aba)
        dataframes.append(df_aba)
    except pd.errors.ParserError:
        pass  # Ignorar a aba se ela não existir

# Se a lista de DataFrames não estiver vazia, concatene-os
if dataframes:
    dados_mesclados = pd.concat(dataframes, ignore_index=True)
else:
    dados_mesclados = pd.DataFrame()

# Selecionar apenas as colunas desejadas
dados_mesclados = dados_mesclados[['Item', 'Cidade', 'Quantidade']]

# Normalizar os nomes das cidades para minúsculas
dados_mesclados['Cidade'] = dados_mesclados['Cidade'].str.lower()

# Agrupar por 'Cidade' e 'Item' e somar as quantidades
df_agrupado = dados_mesclados.groupby(['Cidade', 'Item'], as_index=False).agg({'Quantidade': 'sum'})

# Calcular a quantidade total de cada item
quantidade_por_item = df_agrupado.groupby('Item')['Quantidade'].sum()

# Criar um dicionário para armazenar as quantidades de cada item por cidade
dados_grafico = {}
for _, row in df_agrupado.iterrows():
    cidade = row['Cidade']
    item = row['Item']
    quantidade = row['Quantidade']

    if cidade not in dados_grafico:
        dados_grafico[cidade] = {}

    dados_grafico[cidade][item] = quantidade

# Preparar os dados para o gráfico de barras empilhadas
cidades = list(dados_grafico.keys())
itens = list(dados_mesclados['Item'].unique())
quantidades_por_cidade = {cidade: [dados.get(item, 0) for item in itens] for cidade, dados in dados_grafico.items()}

# Criar o gráfico de barras empilhadas
fig, ax = plt.subplots()

# Criar um mapa de cores
cores = plt.cm.Paired(range(len(itens)))

# Plotar as barras empilhadas
bottom = [0] * len(cidades)
for i, item in enumerate(itens):
    quantidades = [quantidades_por_cidade[cidade][i] for cidade in cidades]
    bars = ax.bar(cidades, quantidades, label=item, bottom=bottom, color=cores[i])
    bottom = [bottom[j] + quantidades[j] for j in range(len(cidades))]

    # Adicionar rótulos de quantidade nas barras
    for bar, quantidade in zip(bars, quantidades):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(quantidade), ha='center', va='bottom')

# Adicionar uma legenda com os nomes dos itens
plt.legend(title='Itens', loc='upper left', bbox_to_anchor=(1, 1))

# Adicionar a quantidade total de cada item no título
titulo_grafico = 'Distribuição de Itens por Cidade\n'
for item, quantidade in quantidade_por_item.items():
    titulo_grafico += f'{item}: {quantidade}\n'

plt.title(titulo_grafico)
plt.xticks(rotation=20)

img_path = "marca-dagua-2.png"
img = plt.imread(img_path)
imagebox = OffsetImage(img, zoom=0.060, resample=True, clip_path=None, clip_box=None, alpha=0.5)
ab = AnnotationBbox(imagebox, (0, 1.090), frameon=False, xycoords='axes fraction', boxcoords="axes fraction")
plt.gca().add_artist(ab)

plt.show()
