# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os

st.set_page_config(page_title="Trabalho 1: Telemetria EDA", layout="wide", page_icon="📊")

st.markdown("<style>h1, h2, h3 { color: #A50034 !important; font-weight: 700; }</style>", unsafe_allow_html=True)
st.title("📊 Trabalho 1: Mineração e Telemetria EDA")
st.caption("LG Electronics AX Academy | Diagnóstico de Ingestão e Estruturação Segura")
st.markdown("---")

CAMINHO_DATASET = "data/dataset_phishing.csv"

if not os.path.exists(CAMINHO_DATASET):
    st.error("🚨 Base de dados de origem 'dataset_phishing.csv' não encontrada na pasta 'data/'.")
    st.stop()

@st.cache_data
def carregar_dados_t1():
    df = pd.read_csv(CAMINHO_DATASET, on_bad_lines='skip', engine='python')
    # Sanitização idêntica do cabeçalho
    df.columns = [c.split(';')[0].strip() for c in df.columns]
    
    if 'status' in df.columns:
        df['target_num'] = df['status'].apply(lambda x: 1 if str(x).strip() == 'phishing' else 0)
    else:
        df['target_num'] = df.get('target', np.zeros(len(df)))
    return df

df_full = carregar_dados_t1()

st.subheader("📋 Auditoria das Amostras Ingeridas (Dataset Base)")
st.dataframe(df_full.head(100), use_container_width=True)

st.markdown("---")
col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    st.markdown("### **Volumetria Global da Variável Alvo**")
    # Forçado para 'status' limpo corrigido
    fig_pie = px.pie(df_full, names='status', color_discrete_sequence=["#A50034", "#686A6F"], hole=0.4)
    st.plotly_chart(fig_pie, use_container_width=True)

with col_graf2:
    st.markdown("### **Associação Linear de Pearson (Top 10 Atributos)**")
    X_num = df_full.select_dtypes(include=['number']).drop(columns=['target_num'], errors='ignore')
    if not X_num.empty:
        correlacoes = X_num.corrwith(df_full['target_num']).abs().sort_values(ascending=False).head(10)
        fig_bar = px.bar(correlacoes, orientation='h', color_discrete_sequence=["#A50034"])
        fig_bar.update_layout(showlegend=False, yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig_bar, use_container_width=True)