from utils.menu import menu_de_opcoes
from utils.config import configurar_pagina
from telas.historico import render_historico
from telas.nova_transacao import render_nova_transacao
from telas.dashboard import render_dashboard


configurar_pagina("Personal Finance", "💼")
pagina = menu_de_opcoes(["Dashboard", "Nova Transação", "Histórico"])


if pagina == "Dashboard":
    render_dashboard()

elif pagina == "Nova Transação":
    render_nova_transacao()

elif pagina == "Histórico":
    render_historico()
