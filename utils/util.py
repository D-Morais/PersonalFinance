from streamlit import cache_data
from repositorio.script_db import carregar_transacoes_df


@cache_data
def carregar_transacoes():
    return carregar_transacoes_df()


def iniciar_sessoes():
    session_state.sugestao = ""
