import pandas as pd

# Carregar o arquivo CSV original
df = pd.read_csv("main-data.csv")

# Definir o ano que deseja filtrar
ano_desejado = 2020

# Filtrar os dados pelo ano desejado
df_filtrado = df[df['year'] == ano_desejado]

# Selecionar apenas as colunas especificadas
df_filtrado = df_filtrado[['num_pushers', 'language', 'language_type', 'iso2_code', 'year', 'quarter']]

# Salvar os dados filtrados em um novo arquivo CSV
df_filtrado.to_csv(f"year-filter/year-filter-{ano_desejado}.csv", index=False)

print("Novo arquivo CSV criado com sucesso!")
