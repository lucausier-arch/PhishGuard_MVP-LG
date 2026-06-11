# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
import os
import sys
import importlib.util
import plotly.graph_objects as go
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

st.set_page_config(page_title="Trabalho 3: MVP Gateway", layout="wide", page_icon="🎲")
st.markdown("<style>h1, h2, h3 { color: #A50034 !important; font-weight: 700; }</style>", unsafe_allow_html=True)

st.title("🛡️ Trabalho 3: Produto Mínimo Viável (MVP)")
st.caption("Filtro Ativo de Borda com Simulação de Dados Inéditos da Banca Examinadora")
st.markdown("---")

CAMINHO_BANCA = "data/dataset2_banca.csv"
CAMINHO_MOTOR = "src/3_motor_predição.py"

if not os.path.exists(CAMINHO_BANCA):
    st.warning("📋 Lote de teste cego ausente na pasta data/. Execute primeiro 'python data/criar_lote_teste.py'.")
    st.stop()

@st.cache_resource
def iniciar_gateway_borda():
    spec = importlib.util.spec_from_file_location("motor_predicao", CAMINHO_MOTOR)
    module = importlib.util.module_from_spec(spec)
    sys.modules["motor_predicao"] = module
    spec.loader.exec_module(module)
    return module.GatewayBordaMle()

try:
    gateway = iniciar_gateway_borda()
except Exception as e:
    st.error(f"❌ Erro ao carregar o modelo campeão: {e}")
    st.info("Certifique-se de executar o arquivo 'src/2_modelagem_avancada.py' para gerar o binário na pasta 'models/'.")
    st.stop()

# Entrada de URL Individual
st.subheader("🌐 Escaneamento Preventivo de URL Avulsa")
url_digitada = st.text_input("Insira uma URL externa para auditoria preditiva instantânea:", placeholder="ex: www.lg-security-panel.net")

if url_digitada:
    prob, veridito, classe = gateway.analisar_link(url_digitada)
    score = prob * 100
    
    c_txt, c_gt = st.columns([2, 1])
    with c_txt:
        if classe == 1:
            st.error(f"🚨 MEDIDA DE SEGURANÇA: {veridito} (Risco Calculado: {score:.1f}%)")
            st.markdown("> **Alerta:** Domínio suspeito interceptado e bloqueado proativamente pela inteligência de borda.")
        else:
            st.success(f"🟢 TRÁFEGO LIBERADO: {veridito} (Risco Calculado: {score:.1f}%)")
            st.markdown("> **Mensagem Amigável:** Link verificado e seguro. Sempre fique de olho e reporte anomalias ao time de TI corporativo!")
            
    with c_gt:
        fig_g = go.Figure(go.Indicator(
            mode="gauge+number", value=score,
            gauge={'axis': {'range': [0, 100]}, 'bar': {'color': "#A50034"},
                   'steps': [{'range': [0, 35], 'color': "#22c55e"}, {'range': [35, 100], 'color': "salmon"}]}))
        fig_g.update_layout(height=180, margin=dict(l=10, r=10, t=10, b=10))
        st.plotly_chart(fig_g, use_container_width=True)

st.markdown("---")

# Simulação por Slider para a Banca
st.subheader("🕹️ Teste de Estresse Interativo da Banca Examinadora")
percentual = st.slider("Fração volumétrica aleatória do lote oculto (%):", 5, 100, 20, step=5)

if st.button("🚀 Processar Amostra em Tempo Real"):
    df_banca = pd.read_csv(CAMINHO_BANCA)
    df_amostra = df_banca.sample(frac=percentual/100.0, random_state=42)
    
    urls = df_amostra['url'].tolist()
    y_reais = df_amostra['target'].tolist()
    
    preds, probs = [], []
    for u in urls:
        p, _, c = gateway.analisar_link(u)
        probs.append(p)
        preds.append(c)
        
    df_amostra['Probabilidade'] = probs
    df_amostra['Gabarito Real'] = np.where(np.array(y_reais) == 1, "🚨 Phishing", "✅ Legítimo")
    df_amostra['Ação do Gateway'] = np.where(np.array(preds) == 1, "❌ BARRADO", "🟢 LIBERADO")
    
    st.dataframe(df_amostra[['url', 'Gabarito Real', 'Ação do Gateway', 'Probabilidade']], use_container_width=True, hide_index=True)
    
    st.subheader("📊 Eficiência em Tempo Real da Amostra Selecionada")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Acurácia Global", f"{accuracy_score(y_reais, preds)*100:.1f}%")
    m2.metric("Precisão Operacional", f"{precision_score(y_reais, preds, zero_division=0)*100:.1f}%")
    m3.metric("Recall (Escudo Protetor)", f"{recall_score(y_reais, preds, zero_division=0)*100:.1f}%")
    m4.metric("F1-Score (Equilíbrio Ouro)", f"{f1_score(y_reais, preds, zero_division=0)*100:.1f}%")