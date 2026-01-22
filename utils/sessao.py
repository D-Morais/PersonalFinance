from streamlit import session_state


def iniciar_session_state():
    session_state.menu = ""
    session_state.sugestao = ""
    session_state.pagina = 0
