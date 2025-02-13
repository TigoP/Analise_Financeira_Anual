import plotly.express as px

def criar_grafico_barras(df):

    return px.bar(df, x='mes', y=['receita', 'despesa', 'lucro_liquido'],
                     title= "Receita, Despesa e Lucro Liquido por Mes",
                     labels={'value': 'Valor (R$)', 'variable': 'Categoria'})

def criar_grafico_linhas(df):

    return px.line(df, x='mes', y='lucro_liquido', title="Evolucao do Lucro ao Longo do Ano")
