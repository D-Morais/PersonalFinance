import sqlite3 as sql
from pandas import read_sql


def criar_conexao():
    return sql.connect(r"db\finance.db")


def iniciar_db():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS transacoes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            valor REAL NOT NULL,
            categoria TEXT NOT NULL,
            tipo_transacao TEXT 
                CHECK(tipo_transacao IN ('renda', 'despesa')) NOT NULL,
            data_transacao DATE NOT NULL
        );
        """
    )

    conexao.commit()
    conexao.close()


def adicionar_transacao(nova_descricao, novo_valor, categoria, transacao, data) -> bool:
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO transacoes (descricao, valor, categoria, tipo_transacao, data_transacao)
            VALUES (?, ?, ?, ?, ?)
            """, (nova_descricao, novo_valor, categoria, transacao, data)
        )
        conexao.commit()
        return True

    except conexao.IntegrityError:
        conexao.rollback()
        return False

    finally:
        conexao.close()


def buscar_todas_transacoes():
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM transacoes")

    linhas = cursor.fetchall()
    conexao.close()

    return linhas


def carregar_transacoes_df():
    conexao = criar_conexao()
    query = """
        SELECT descricao, valor, categoria, tipo_transacao, data_transacao
        FROM transacoes
        ORDER BY data_transacao DESC
    """
    df = read_sql(query, conexao)
    conexao.close()
    return df


if __name__ == "__main__":
    iniciar_db()
