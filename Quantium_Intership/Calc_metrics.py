import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_transacoes = pd.read_excel('Job_Files/QVI_transaction_data.xlsx')
df_clientes = pd.read_csv('Job_Files/QVI_purchase_behaviour.csv')

print(df_transacoes.columns)

print(df_clientes.columns)

print(df_transacoes.head())

print(df_clientes.head())


df_total = pd.merge(df_transacoes, df_clientes, on='LYLTY_CARD_NBR', how='inner')

df_total.info()

df_total.isna().sum()

df_total.duplicated().sum()

df_total.describe()

segmentos = df_total.groupby(['LIFESTAGE', 'PREMIUM_CUSTOMER'])


analise_segmento = segmentos.agg(
    Faturamento_Total=('TOT_SALES', 'sum'),
    Total_Pacotes=('PROD_QTY', 'sum'),
    Clientes_Unicos=('LYLTY_CARD_NBR', 'nunique')
).reset_index()


analise_segmento['Preco_Medio_Pacote'] = analise_segmento['Faturamento_Total'] / analise_segmento['Total_Pacotes']
analise_segmento['Pacotes_Por_Cliente'] = analise_segmento['Total_Pacotes'] / analise_segmento['Clientes_Unicos']

analise_segmento = analise_segmento.sort_values(by='Faturamento_Total', ascending=False)



print(df_transacoes['LYLTY_CARD_NBR'].nunique())
print(df_clientes['LYLTY_CARD_NBR'].nunique())
print(df_total['LYLTY_CARD_NBR'].nunique())
print(df_total['PROD_QTY'].describe())
print(df_total['TOT_SALES'].describe())
print(df_total['PROD_NAME'].nunique())
print(df_total['LIFESTAGE'].value_counts())
print(df_total['PREMIUM_CUSTOMER'].value_counts())


# =====================================================
# 5. INVESTIGAÇÃO DE OUTLIERS
# =====================================================


print(
    df_total.nlargest(
        10,
        "PROD_QTY"
    )[

    [
    "LYLTY_CARD_NBR",
    "PROD_NAME",
    "PROD_QTY",
    "TOT_SALES"
    ]
]
)