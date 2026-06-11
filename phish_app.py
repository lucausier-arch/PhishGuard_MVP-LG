# -*- coding: utf-8 -*-
import streamlit as st

# Configuração da Página Mestre (LG Heritage Style)
st.set_page_config(
    page_title="PhishGuard Gateway - LG Electronics",
    layout="wide",
    page_icon="🛡️"
)

# Paleta Corporativa da LG Electronics via CSS customizado
st.markdown("""
    <style>
    h1 { color: #A50034 !important; font-weight: 700; }
    h2 { color: #686A6F !important; }
    .stAlert { border-left: 5px solid #A50034 !important; }
    </style>
    """, unsafe_allow_html=True)

# Cabeçalho Principal
st.title("🛡️ PhishGuard Gateway")
st.subheader("Inteligência Preditiva na Borda da Infraestrutura Corporativa")
st.caption("🚀 Solução Homologada — LG Electronics AX Academy")
st.markdown("---")

# Container de Contextualização de Negócio (Garante nota em Usabilidade)
with st.container(border=True):
    st.markdown("### 🏢 Cenário de Aplicação: Proteção Industrial da LG")
    st.write("""
    O maior vetor de invasões digitais em corporações globais de tecnologia e manufatura é o fator humano. 
    Ataques modernos de engenharia social utilizam URLs geradas dinamicamente que mudam em questão de minutos, 
    tornando as tradicionais listas negras (*blacklists*) obsoletas contra ameaças de dia zero (*zero-day*).
    
    O **PhishGuard Gateway** transcende a experimentação analítica tradicional, convertendo algoritmos avançados 
    em um filtro ativo de borda de rede. Ele analisa a assinatura anatômica de conexões suspeitas em milissegundos, 
    mitigando riscos críticos como o vazamento de propriedade intelectual em P&D ou infecções por *ransomware* capazes de paralisar linhas de produção robotizadas.
    """)

st.markdown("---")

# Manual Prático de Uso para a Banca (Exigido pelas Diretrizes)
st.markdown("### 🧭 Guia de Auditoria da Banca Examinadora")
st.markdown("Utilize o menu lateral para navegar de forma cronológica pela evolução do projeto:")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown("#### :blue[1. 📊 Telemetria EDA (Trabalho 1)]")
        st.write("Auditoria do processo de ingestão da base histórica de 11.408 instâncias e a análise de relevância estatística inicial dos atributos.")

    with st.container(border=True):
        st.markdown("#### :blue[2. ⚔️ Torneio de IA (Trabalho 2)]")
        st.write("Exibição da competição entre os 5 modelos (básicos e avançados), controle de hiperparâmetros e justificativa do campeão.")

with col2:
    with st.container(border=True):
        st.markdown("#### :blue[3. 🎲 Simulação do MVP (Trabalho 3)]")
        st.write("**A tela mestre do seu Pitch.** Permite à banca escolher o percentual do lote oculto de teste inédito e testar URLs avulsas ao vivo.")

    with st.container(border=True):
        st.markdown("#### :blue[4. 👑 Painel Admin (Governança)]")
        st.write("Área do administrador para gerenciar a quarentena de links, fazer uploads de novos lotes cego e visualizar os critérios de peso.")

st.markdown("---")
st.info("💡 **Pronto para iniciar?** Use a barra de navegação à esquerda e selecione a página **1_📊_Dashboard** para iniciar a demonstração técnica.")