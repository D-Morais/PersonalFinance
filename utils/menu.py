import streamlit as st


def menu_de_opcoes(opcoes: list) -> str:
    if "menu" not in st.session_state:
        st.session_state.menu = opcoes[0]

    with st.sidebar:
        st.title("💼 Personal Finance")
        selected = st.sidebar.radio(
            "",
            opcoes,
            horizontal=False,
            index=opcoes.index(st.session_state.menu)
        )

        st.session_state.menu = selected
        return selected
