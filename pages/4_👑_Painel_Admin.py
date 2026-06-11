# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Painel de Administração", layout="wide", page_icon="👑")

st.title("👑 Módulo de Governança do Administrador")
st.caption("Acesso Restrito — Controle de Políticas Corporativas de Segurança da LG Electronics")
st.markdown("---")

# Container customizado com borda azul para a área administrativa
with st.container(border=True):
    st.markdown("### :blue[⚙️ Ajuste Fino dos Parâmetros de Quarentena]")
    st.write("Modifique o limiar operativo do motor preditivo para alterar a sensibilidade do escudo de proteção:")
    limiar_ativo = st.slider("Calibração de Limiar de Risco Ativo (Threshold):", 0.10, 0.90, 0.35, step=0.05)
    st.info(f"O limiar atual está fixado de forma robusta em **{limiar_ativo}** para priorizar a captura total de ameaças industriais.")

st.markdown("---")
st.subheader("📐 Critérios e Pesos de Detecção do Phishing")
st.markdown("Tabela estrutural demonstrando como a Inteligência de Borda pontua os elementos anatômicos das 87 colunas:")

df_pesos = pd.DataFrame({
    "Indicador Técnico": ["length_url", "nb_dots", "nb_hyphens", "https_token", "ip_in_url"],
    "Propriedade Anatômica da URL": ["Comprimento total dos caracteres da string", "Contagem de pontos presentes no domínio", "Densidade de hífens agregados", "Presença de assinatura token SSL válida", "Uso de endereço IP direto substituindo o Hostname"],
    "Peso Concedido pelos Robôs": ["Médio Impacto Positivo", "Alto Impacto Positivo", "Baixo Impacto Positivo", "Crítico Redutor de Risco (Negativo)", "Bloqueio Imediato de Tráfego"]
})
st.table(df_pesos)

st.markdown("---")
st.subheader("📥 Ingestão de Novos Lotes de Auditoria")
st.markdown("Arraste um novo conjunto de teste cego (`dataset2.csv`) enviado pela banca para atualizar o monitor operativo:")

arquivo_carregado = st.file_uploader("Selecionar arquivo de dados inéditos no formato .csv", type=["csv"])

if arquivo_carregado is not None:
    df_novo_lote = pd.read_csv(arquivo_carregado)
    st.success(f"✔️ Arquivo de auditoria carregado com sucesso! Mapeados {df_novo_lote.shape[0]} novos links de teste.")