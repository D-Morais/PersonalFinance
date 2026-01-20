from streamlit import set_page_config


def configurar_pagina(titulo: str, icon: str) -> None:
    set_page_config(
        page_title=titulo,
        page_icon=icon,
        layout="wide",
        initial_sidebar_state="auto"
    )

