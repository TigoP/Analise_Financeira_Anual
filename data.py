import pandas as pd

def carregar_dados():

    data = {
        'Mes': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
        'Receita': [100000, 120000, 130000, 110000, 105000, 115000, 125000, 135000, 140000, 145000, 150000, 160000],
        'Despesa': [60000, 65000, 70000, 67000, 69000, 75000, 80000, 85000, 88000, 90000, 95000, 100000],
        'Impostos': [10000, 12000, 13000, 11000, 11500, 12000, 12500, 13000, 13500, 14000, 14500, 15000],
    }

    df = pd.DataFrame(data)
    df['Lucro Liquido'] = df['Receita'] - df['Despesa'] - df['Impostos']
    df['Margem de Lucro'] = (df['Lucro Liquido'] / df['Receita']) * 100

    return df
