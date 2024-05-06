import pandas as pd
from tabulate import tabulate

# Carregar o arquivo CSV
df = pd.read_csv("main-data.csv")

# Filtrar os dados onde o tipo de linguagem é "programming"
programming_df = df[df['language_type'] == 'programming']

# Calcular a mediana para cada linguagem de programação
median_by_language = programming_df.groupby('language')['num_pushers'].median()

# Encontrar as 6 maiores medianas
top_6_medians = median_by_language.nlargest(6)

# Lista das top 6 linguagens por mediana
top_6_languages = top_6_medians.index.tolist()

# Filtrar os dados apenas para as top 6 linguagens
filtered_data_top_6 = programming_df[programming_df['language'].isin(top_6_languages)]

# Calcular a mediana de 'num_pushers' por linguagem e ano para as top 6 linguagens
median_by_language_year_top_6 = filtered_data_top_6.groupby(['language', 'year'])['num_pushers'].median().unstack()

# Adicionar a mediana geral (para todos os anos) como uma nova coluna
median_by_language_year_top_6['Overall Median'] = median_by_language.loc[top_6_languages]

# Resetar o índice para facilitar a formatação da tabela
median_by_language_year_top_6.reset_index(inplace=True)

# Reordenar as colunas para colocar 'Overall Median' por último
columns = list(median_by_language_year_top_6.columns)
columns.remove('Overall Median')
columns.append('Overall Median')
median_by_language_year_top_6 = median_by_language_year_top_6[columns]

# Ordenar as linguagens de acordo com a mediana geral (em ordem decrescente)
median_by_language_year_top_6.sort_values(by='Overall Median', ascending=False, inplace=True)

# Formatar a tabela diretamente usando tabulate
headers = ['Language'] + [f'Median pushers ({year})' for year in median_by_language_year_top_6.columns[1:-1]] + ['Overall Median']
table_formatted = tabulate(median_by_language_year_top_6.values, headers=headers, tablefmt='rounded_outline', floatfmt='.2f')

# Imprimir a tabela formatada
print(table_formatted)
