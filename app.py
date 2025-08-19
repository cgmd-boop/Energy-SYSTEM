
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Gestão de Energia da Fábrica", layout="wide")
st.title("🔋 Sistema de Gestão de Energia da Fábrica")

# Menu lateral
menu = st.sidebar.selectbox("📁 Selecione uma opção", [
    "Registro de Quedas de Energia",
    "Contas de Água e Energia",
    "Agendamento de Manutenções",
    "Análise de Gráficos",
    "Indicadores ESG, QSMS e ISO 50001",
    "Painel de Monitoramento",
    "Relatório Estratégico"
])

# Função auxiliar para calcular variação percentual
def calcular_variacao(valores):
    if len(valores) < 2 or valores[-2] == 0:
        return 0
    return ((valores[-1] - valores[-2]) / valores[-2]) * 100

# Registro de quedas de energia
if menu == "Registro de Quedas de Energia":
    st.subheader("⚡ Registrar Queda de Energia")
    data_queda = st.date_input("Data da Queda")
    hora_queda = st.time_input("Horário da Queda")
    hora_retorno = st.time_input("Horário de Retorno")
    causa = st.selectbox("Causa", ["Interna", "Externa"])

    protocolo = ""
    responsavel = ""
    motivo_interno = ""

    if causa == "Externa":
        protocolo = st.text_input("Protocolo da Concessionária")
        responsavel = st.text_input("Responsável pelo Chamado")
    elif causa == "Interna":
        motivo_interno = st.text_input("Motivo da Queda Interna")

    if st.button("Registrar"):
        st.success("✅ Queda de energia registrada com sucesso.")
        if causa == "Externa":
            st.info(f"Protocolo: {protocolo} | Responsável: {responsavel}")
        elif causa == "Interna":
            st.info(f"Motivo: {motivo_interno}")

# Contas de água e energia
elif menu == "Contas de Água e Energia":
    st.subheader("💰 Registrar Conta")
    tipo_conta = st.selectbox("Tipo de Conta", ["Energia", "Água"])
    data_conta = st.date_input("Data da Conta")
    valor_conta = st.number_input("Valor da Conta (R$)", min_value=0.0)
    multa = st.checkbox("Houve multa?")
    if st.button("Salvar Conta"):
        st.success("✅ Conta registrada com sucesso.")

# Agendamento de manutenções
elif menu == "Agendamento de Manutenções":
    st.subheader("🛠️ Agendar Manutenção")
    tipo_manutencao = st.selectbox("Tipo de Manutenção", ["Corretiva", "Preditiva"])
    data_manutencao = st.date_input("Data da Manutenção")
    motivo = st.text_input("Motivo")
    status = st.selectbox("Status", ["Em andamento", "Parado", "Finalizado"])
    if st.button("Agendar"):
        st.success("✅ Manutenção agendada com sucesso.")

# Análise de gráficos com Plotly
elif menu == "Análise de Gráficos":
    st.subheader("📊 Análise de Gráficos")
    meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]
    energia = np.random.randint(1000, 1500, size=len(meses))
    agua = np.random.randint(250, 350, size=len(meses))
    df = pd.DataFrame({"Mês": meses, "Energia (kWh)": energia, "Água (m³)": agua})

    fig1 = px.line(df, x="Mês", y="Energia (kWh)", title="Consumo de Energia")
    fig2 = px.bar(df, x="Mês", y="Água (m³)", title="Consumo de Água")

    st.plotly_chart(fig1, use_container_width=True)
    st.plotly_chart(fig2, use_container_width=True)

# Indicadores ESG, QSMS e ISO 50001
elif menu == "Indicadores ESG, QSMS e ISO 50001":
    st.subheader("📈 Indicadores ESG, QSMS e ISO 50001")
    indicador = st.selectbox("Selecione o Indicador", ["ESG", "QSMS", "ISO 50001"])
    st.info(f"Análise dinâmica do indicador {indicador}")
    status = np.random.choice(["Tudo OK", "Em Atenção", "Estado Crítico"])
    st.metric("Status Atual", status)
    if status == "Estado Crítico":
        st.warning("⚠️ Sugestão: Realizar auditoria interna e revisar processos.")

# Painel de monitoramento
elif menu == "Painel de Monitoramento":
    st.subheader("🛰️ Painel de Monitoramento")
    st.write("📍 Localização: Av. Dr. Júlio Maranhão 3219, Jaboatão dos Guararapes, PE, 54325-440")
    parametro = st.selectbox("Parâmetro", ["Energia", "Água", "Manutenção", "Indicadores"])
    st.write(f"🔍 Pontos de interesse sobre o parâmetro **{parametro}**")
    st.write("📡 Visualização em tempo real dos dados e status.")

# Relatório estratégico
elif menu == "Relatório Estratégico":
    st.subheader("📄 Relatório Estratégico")
    st.write("Resumo dos dados registrados para análise estratégica.")
    st.download_button("📥 Baixar Relatório", data="Resumo dos dados registrados...", file_name="relatorio_estrategico.txt")


st.markdown(...)
pandas
numpy
plotly


