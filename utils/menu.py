import streamlit as st


def menu_de_opcoes(opcoes):
    if "menu" not in st.session_state:
        st.session_state.menu = options[0]

    with st.sidebar:
        st.title("💼 Personal Finance")
        selected = st.sidebar.radio(
            "",
            options,
            horizontal=False,
            index=options.index(st.session_state.menu)
        )

        st.session_state.menu = selected
        return selected
