import streamlit as st
import pandas as pd


def render_historico() -> None:

    st.title("📜 Histórico de Transações")

    df = carregar_transacoes_df()

    if df.empty:
        st.warning("Nenhuma transação cadastrada.")
        return

    # ===============================
    # 🔎 FILTROS
    # ===============================

    st.sidebar.header("🔎 Filtros")

    # Tipo
    tipo = st.sidebar.selectbox(
        "Tipo",
        ["Todos", "Renda", "Despesa"]
    )
    if tipo == "Renda":
        tipo = "renda"
    elif tipo == "Despesa":
        tipo = "despesa"

    # Categoria
    categorias = ["Todas"] + sorted(df["categoria"].unique().tolist())
    categoria = st.sidebar.selectbox("Categoria", categorias)

    # Período
    df["data_transacao"] = pd.to_datetime(df["data_transacao"])

    data_min = df["data_transacao"].min().date()
    data_max = df["data_transacao"].max().date()

    data_ini = st.sidebar.date_input("Data inicial", data_min, format="DD/MM/YYYY")
    data_fim = st.sidebar.date_input("Data final", data_max, format="DD/MM/YYYY")

    # ===============================
    # 🔄 APLICA FILTROS
    # ===============================

    filtro = df.copy()

    if tipo != "Todos":
        filtro = filtro[filtro["tipo_transacao"] == tipo]

    if categoria != "Todas":
        filtro = filtro[filtro["categoria"] == categoria]

    filtro = filtro[
        (filtro["data_transacao"] >= pd.to_datetime(data_ini)) &
        (filtro["data_transacao"] <= pd.to_datetime(data_fim))
        ]

    # ===============================
    # 📑 PAGINAÇÃO
    # ===============================

    st.subheader("📋 Transações")

    ITENS_POR_PAGINA = 20

    if "pagina" not in st.session_state:
        st.session_state.pagina = 0

    inicio = st.session_state.pagina * ITENS_POR_PAGINA
    fim = inicio + ITENS_POR_PAGINA

    pagina_df = filtro.iloc[inicio:fim]
    pagina_df = pagina_df.rename(columns={
        "descricao": "Descrição",
        "valor": "Valor",
        "categoria": "Categoria",
        "tipo_transacao": "Tipo",
        "data_transacao": "Data"
    })
    pagina_df["Data"] = pagina_df["Data"].dt.strftime("%d-%m-%Y")
    st.dataframe(
        pagina_df, hide_index=True,
        use_container_width=True
    )

    # ===============================
    # ⏭ CONTROLES
    # ===============================

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("⬅ Anterior") and st.session_state.pagina > 0:
            st.session_state.pagina -= 1

    with col2:
        st.write(
            f"Página {st.session_state.pagina + 1} "
            f"de {((len(filtro) - 1) // ITENS_POR_PAGINA) + 1}"
        )

    with col3:
        if st.button("Próximo ➡") and fim < len(filtro):
            st.session_state.pagina += 1