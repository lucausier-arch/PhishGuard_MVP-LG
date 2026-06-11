# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import json
import os
import plotly.express as px

st.set_page_config(page_title="Trabalho 2: Torneio de IA", layout="wide", page_icon="⚔️")
st.markdown("<style>h1, h2, h3 { color: #A50034 !important; font-weight: 700; }</style>", unsafe_allow_html=True)

st.title("⚔️ Trabalho 2: O Torneio dos 5 Soldados")
st.caption("Aferição Multimétrica de Desempenho dos Robôs Caçadores de Links")
st.markdown("---")

# Caminho dinâmico para evitar confusões de execução do Streamlit Runtime
DIRETORIO_PAGINA = os.path.dirname(os.path.abspath(__file__))
RAIZ_PROJETO = os.path.dirname(DIRETORIO_PAGINA)
CAMINHO_METRICAS = os.path.join(RAIZ_PROJETO, "models", "metricas_torneio.json")

if not os.path.exists(CAMINHO_METRICAS):
    st.error(f"📋 Arquivo ausente em: {CAMINHO_METRICAS}")
    st.info("Abra o terminal do VS Code e digite: python src/2_modelagem_avancada.py")
    st.stop()

# Força a re-leitura do arquivo ignorando qualquer cache do navegador
with open(CAMINHO_METRICAS, "r") as f:
    metricas = json.load(f)

df_metricas = pd.DataFrame(metricas).T.reset_index().rename(columns={"index": "Robô Soldado"})

st.subheader("🏆 Tabela Comparativa de Eficiência (As 5 Notas)")
st.dataframe(df_metricas, use_container_width=True, hide_index=True)

st.markdown("---")
st.subheader("📊 Gráfico Interativo de Desempenho do Time")
fig_torneio = px.bar(df_metricas, x="Robô Soldado", 
                     y=["F1-Score (Equilíbrio)", "Recall (Escudo Protetor)", "Precisão (Sem Alarme Falso)", "ROC-AUC (Superpoder)", "Log Loss (Confiança)"], 
                     barmode="group", title="Aferição Estatística de Capacidade Preditiva",
                     color_discrete_sequence=["#A50034", "#686A6F", "#22c55e", "#3b82f6", "#eab308"])
st.plotly_chart(fig_torneio, use_container_width=True)

st.markdown("---")
st.subheader("📉 Zona de Crítica e Eliminação dos 'Perdedores'")
with st.container(border=True):
    st.markdown("""
    * **Naive Bayes (O Contador):** Falhou pelo excesso de alarmes falsos em ambientes industriais reais.
    * **Regressão Logística & Árvore Binária:** Baixa capacidade adaptativa para links gerados por robôs maliciosos.
    """)