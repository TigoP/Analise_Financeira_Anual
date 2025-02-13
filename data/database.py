import os
import logging
import pandas as pd
import mysql.connector

from decimal import Decimal
from dotenv import load_dotenv

load_dotenv()

def conectar_db():
    try:
        return mysql.connector.connect(
            host=os.getenv('DB_HOST', "127.0.0.1"),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_DATABASE'),
            use_pure=True,
            unix_socket=None
        )
    except mysql.connector.Error as err:
        logging.error(f"Erro ao conectar com o banco de dados: {err}")
        raise

def obter_dados():
    logging.info("Obtendo dados do banco de dados...")
    conexao = conectar_db()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute('SELECT * FROM dados_fiscais')
    dados = cursor.fetchall()
    conexao.close()
    logging.info(f"Dados carregados com sucesso! {len(dados)} registros retornados.")

    print("Dados retornados: ", dados)

    df = pd.DataFrame(dados)
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]

    for col in ['receita', 'despesa', 'impostos']:
        df[col] = df[col].astype(float)

    df["lucro_liquido"] = df["receita"] - df["despesa"] - df["impostos"]
    df["margem_de_lucro"] = (df["lucro_liquido"] / df["receita"]) * 100

    return df

if __name__ == '__main__':
    try:
        conexao = conectar_db()
        cursor = conexao.cursor()
        cursor.execute('SELECT NOW();')
        print("Conexão com o banco de dados realizada com sucesso!", cursor.fetchone())
    except Exception as e:
        print("Erro ao conectar com o banco de dados!", e)
    conexao.close()
