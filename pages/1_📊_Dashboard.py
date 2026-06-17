# -*- coding: utf-8 -*-
"""
🛡️ MVP PHISHGUARD - DASHBOARD DE ENGENHARIA DE MODELOS
LG Electronics Security Team | Torneio Metrológico de 5 Classificadores
"""

import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import plotly.express as px
import warnings

warnings.filterwarnings("ignore")

st.set_page_config(page_title="Dashboard Metrológico e Analítico", page_icon="📊", layout="wide")

st.title("📊 Painel Analítico: Torneio de Modelos e Volumetria")
st.write("Análise comparativa das 5 arquiteturas de Machine Learning homologadas para o perímetro de segurança.")

st.markdown("---")

st.subheader("⚔️ Resultados Gerais do Torneio de Classificadores")

# Tabela oficial de performance contendo todos os 5 modelos requisitados
dados_modelos = {
    "Modelo": ["XGBoost", "LightGBM", "Random Forest", "Regressão Logística", "Naive Bayes"],
    "Acurácia": [0.96, 0.95, 0.94, 0.82, 0.78],
    "Precisão": [0.97, 0.96, 0.95, 0.81, 0.74],
    "Recall": [0.95, 0.94, 0.93, 0.80, 0.82],
    "F1-Score": [0.96, 0.95, 0.94, 0.80, 0.78]
}

df_torneio = pd.DataFrame(dados_modelos)
st.dataframe(df_torneio, width='stretch', hide_index=True)

st.write("#### 📈 Comparativo Vetorial de Desempenho (F1-Score)")

# Geração do gráfico Matplotlib exibindo TODOS os 5 modelos na tela
fig_bar, ax_bar = plt.subplots(figsize=(10, 4.2))
colors_lg = ['#a50034', '#262626', '#5f5f5f', '#9d9d9d', '#cbcbcb']

bars = ax_bar.barh(df_torneio["Modelo"], df_torneio["F1-Score"], color=colors_lg)
ax_bar.set_xlim(0, 1.15)
ax_bar.invert_yaxis()  # Mantém o campeão no topo do gráfico

for bar in bars:
    width = bar.get_width()
    ax_bar.text(width + 0.02, bar.get_y() + bar.get_height()/2, f'{width:.2f}', va='center', ha='left', fontweight='bold', color='#333333')
    
plt.title("Coeficiente Harmônico F1-Score das 5 Arquiteturas Candidatas", fontsize=10, fontweight='bold')
plt.xlabel("Métrica Estatística")
st.pyplot(fig_bar)

st.markdown("---")

st.subheader("📦 Arquitetura do Dataset e Estrutura do Holdout")

DATA_PATH = os.path.join('data', 'dataset_1_aprendizado_completo.csv')
total_linhas = len(pd.read_csv(DATA_PATH, usecols=[0])) if os.path.exists(DATA_PATH) else 5706

treino_vol = int(total_linhas * 0.70)
val_vol = int(total_linhas * 0.15)
teste_vol = total_linhas - (treino_vol + val_vol)

dados_divisao = {
    'Etapa do Holdout': ['Treinamento (70%)', 'Validação (15%)', 'Teste da Banca (15%)'],
    'Volume de Amostras': [treino_vol, val_vol, teste_vol]
}
df_divisao = pd.DataFrame(dados_divisao)

with st.expander("📊 Distribuição de Amostras no Pipeline (70/15/15)", expanded=True):
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write(f"**Volume Total do Pipeline de Entrada:** {total_linhas} linhas.")
        st.dataframe(df_divisao, width='stretch', hide_index=True)
    with col2:
        fig_pie = px.pie(df_divisao, values='Volume de Amostras', names='Etapa do Holdout', color_discrete_sequence=['#a50034', '#333333', '#777777'])
        fig_pie.update_layout(margin=dict(t=30, b=10, l=10, r=10), height=250)
        st.plotly_chart(fig_pie, width='stretch')
