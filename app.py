import dash

from dash import html, dcc
from data.data import carregar_dados
from plots.plots import criar_grafico_barras, criar_grafico_linhas

df = carregar_dados()

app = dash.Dash(__name__)

app.layout = html.Div(
    [
    html.H1('Analise Fiscal da Empresa', style={'textAlign': 'center'}),

    dcc.Graph(figure=criar_grafico_barras(df)),
    dcc.Graph(figure=criar_grafico_linhas(df)),

    html.H2('Indicadores Financeiros', style={'textAlign': 'center'}),
    html.Div([
        html.P(f"Lucro Liquido Total: R$ {df['lucro_liquido'].sum():,.2f}"),
        html.P(f"Margem de Lucro Media: {df['margem_de_lucro'].mean():,.2f}%")
    ], style={'textAlign': 'center'}),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
