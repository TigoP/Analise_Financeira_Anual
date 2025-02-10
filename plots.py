import plotly.express as px

def criar_grafico_barras(df):

    return px.bar(df, x='Mes', y=['Receita', 'Despesa', 'Lucro Liquido'],
                     title= "Receita, Despesa e Lucro Liquido por Mes",
                     labels={'value': 'Valor (R$)', 'variable': 'Categoria'})

def criar_grafico_linhas(df):

    return px.line(df, x='Mes', y='Lucro Liquido', title="Evolucao do Lucro ao Longo do Ano")
