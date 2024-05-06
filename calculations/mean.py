import pandas as pd
from tabulate import tabulate

# Carregar o arquivo CSV
df = pd.read_csv("main-data.csv")

# Filtrar os dados onde language_type é igual a "programming"
programming_df = df[df['language_type'] == 'programming']

# Calcular a média para cada linguagem de programação
media_por_linguagem = programming_df.groupby('language')['num_pushers'].mean()

# Encontrar as 6 maiores médias
maiores_medias = media_por_linguagem.nlargest(6)

# Lista das 6 maiores linguagens por média
top_6_linguagens = maiores_medias.index.tolist()

# Filtrar dados apenas para as 6 maiores linguagens
filtered_data_top_6 = programming_df[programming_df['language'].isin(top_6_linguagens)]

# Calcular a média de 'num_pushers' por linguagem e ano para as 6 maiores linguagens
media_por_linguagem_ano_top_6 = filtered_data_top_6.groupby(['language', 'year'])['num_pushers'].mean().unstack()

# Adicionar a média geral (todos os anos) como uma nova coluna
media_por_linguagem_ano_top_6['Média Geral'] = media_por_linguagem.loc[top_6_linguagens]

# Resetar o índice para facilitar a formatação da tabela
media_por_linguagem_ano_top_6.reset_index(inplace=True)

# Reordenar as colunas para colocar 'Média Geral' por último
colunas = list(media_por_linguagem_ano_top_6.columns)
colunas.remove('Média Geral')
colunas.append('Média Geral')
media_por_linguagem_ano_top_6 = media_por_linguagem_ano_top_6[colunas]

# Ordenar as linguagens de acordo com a média geral (em ordem decrescente)
media_por_linguagem_ano_top_6.sort_values(by='Média Geral', ascending=False, inplace=True)

# Formatar a tabela diretamente usando tabulate
headers = ['Linguagem'] + [f'Média de pushers ({ano})' for ano in media_por_linguagem_ano_top_6.columns[1:-1]] + ['Média Geral']
tabela_formatada = tabulate(media_por_linguagem_ano_top_6.values, headers=headers, tablefmt='rounded_outline', floatfmt='.2f')

# Imprimir a tabela formatada
print(tabela_formatada)
