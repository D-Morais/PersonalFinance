import sqlite3 as sql


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


if __name__ == "__main__":
    iniciar_db()
