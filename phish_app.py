# -*- coding: utf-8 -*-
"""
🛡️ MVP PHISHGUARD - SISTEMA INTEGRADO DE SEGURANÇA DA INFORMAÇÃO
LG Electronics Security Team | Arquitetura Multipáginas Homologada pela Banca
"""

import streamlit as st
import os
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

# Configuração estável e centralizada da aplicação corporativa
st.set_page_config(page_title="PhishGuard MVP - LG", page_icon="🛡️", layout="wide")

# Inicialização segura do Threshold na memória global de sessão
if 'limiar_calibrado' not in st.session_state:
    st.session_state.limiar_calibrado = 0.50

st.title("🛡️ Projeto PhishGuard: Inteligência Preditiva contra Phishing")
st.subheader("MVP de Segurança Digital Desenvolvido para a LG Electronics")

st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.write("### 🚀 Bem-vindo ao Laboratório Cibernético")
    st.write(
        "O PhishGuard é uma plataforma de governança preditiva projetada para monitorar, "
        "auditar e interceptar ataques de engenharia social disfarçados em URLs de tráfego de rede."
    )
    
    st.info(
        "💡 **Rigor da Arquitetura Metodológica:**\n\n"
        "Navegue pelas páginas do menu lateral para auditar o sistema:\n"
        "- **📊 Dashboard:** Estatísticas consolidadas e volumetria do Holdout.\n"
        "- **🧪 Simulacao Banca:** Testes de estresse volumétricos com cargas de URLs inéditas.\n"
        "- **👑 Painel Admin:** Área autenticada para auditoria do banco de dados e calibração fina do Limiar."
    )

with col2:
    st.write("### 🎛️ Configuração do Sistema")
    st.metric(
        label="🛡️ Limiar Ativo de Bloqueio (Threshold)", 
        value=f"{st.session_state.limiar_calibrado:.2f}",
        help="Este parâmetro é controlado na Área de Administração pelo Gestor de Cibersegurança."
    )
    
    # CORREÇÃO DO ERRO VISUAL: Sincronização exata com as duas planilhas oficiais enviadas
    DATA_1 = os.path.join('data', 'dataset_1_aprendizado_completo.csv')
    DATA_2 = os.path.join('data', 'dataset_2_execucao_cego.csv')
    
    if os.path.exists(DATA_1) and os.path.exists(DATA_2):
        st.success("🟢 Banco de Dados Conectado e Sincronizado.")
    else:
        st.error("⚠️ Atenção: Planilhas oficiais ausentes na pasta /data.")
        st.write("Certifique-se de que os nomes correspondem a `dataset_1_aprendizado_completo.csv` e `dataset_2_execucao_cego.csv`.")

st.write("---")
st.caption("Tecnologia de Proteção de Ativos Digitais - Cyber Security Division, LG Electronics.")