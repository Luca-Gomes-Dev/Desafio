import pandas as pd

df_vacinados = pd.read_csv('vacinados.csv')
df_vacinados1 = df_vacinados.loc[(df_vacinados['sexo'] == 'FEMININO') & ((df_vacinados['raca_cor'] == 'PARDA') | (df_vacinados['raca_cor'] == 'PRETA')) & (df_vacinados['idade'] > 60)]
print(df_vacinados1)

df_vacinados['data_vacinacao'] = pd.to_datetime(df_vacinados['data_vacinacao'])

df_filtro = df_vacinados[(df_vacinados['data_vacinacao'].dt.month.isin([11, 12])) & (df_vacinados['sexo'] == 'MASCULINO')]
print(df_filtro)

