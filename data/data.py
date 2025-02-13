import pandas as pd

from data.database import obter_dados

def carregar_dados():

    dados = obter_dados()
    df = pd.DataFrame(dados)

    df['lucro_liquido'] = df['receita'] - df['despesa'] - df['impostos']
    df['margem_de_lucro'] = (df['lucro_liquido'] / df['receita']) * 100

    meses_ordenados = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    df['mes'] = pd.Categorical(df['mes'], categories=meses_ordenados, ordered=True)
    df = df.sort_values('mes')

    return df
