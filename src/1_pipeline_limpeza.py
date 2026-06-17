# -*- coding: utf-8 -*-
"""
🛡️ MVP PHISHGUARD - PIPELINE DE EXTRAÇÃO E SANITIZAÇÃO COMPLETA
LG Electronics Security Team | Rigor Metodológico com 87 Critérios Numéricos
"""

import os
import warnings
import pandas as pd

warnings.filterwarnings("ignore", category=UserWarning)

print("⚡ [T1] Inicializando o pipeline de limpeza estrutural dos critérios...")

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
RAIZ_PROJETO = os.path.dirname(DIRETORIO_ATUAL)
PASTA_DATA = os.path.join(RAIZ_PROJETO, "data")
caminho_bruto = os.path.join(PASTA_DATA, "dataset_1_aprendizado_completo.csv")

if not os.path.exists(caminho_bruto):
    raise FileNotFoundError(f"⚠️ Planilha de aprendizado não localizada em: {caminho_bruto}")

# Leitura tratando linhas instáveis ou delimitadores extras do Excel
df = pd.read_csv(caminho_bruto, on_bad_lines='skip')

# Remove colunas fantasmas que o Excel cria ao final da planilha
df = df.loc[:, ~df.columns.str.contains('^unnamed', case=False)]

# Padroniza rigorosamente o nome de todas as colunas para letras minúsculas
df.columns = [str(c).split(';')[0].strip().lower() for c in df.columns]

# Identifica a coluna alvo (status/gabarito)
coluna_alvo = [c for c in df.columns if 'status' in c or 'label' in c or 'target' in c][-1]

# REMOÇÃO DE VALORES NULOS: Remove linhas onde a URL ou o Status estejam vazios
df = df.dropna(subset=['url', list(df.columns)[-1]])

# Converte o status em bit puro (1 para Phishing, 0 para Veridico)
df[coluna_alvo] = df[coluna_alvo].astype(str).apply(
    lambda x: 1 if 'phish' in x.lower() or '1' in x.lower() else 0
)

# Coerção de tipos: Garante que todos os 87 critérios numéricos sejam inteiros limpos e sem NaNs
colunas_numericas = df.columns.drop(['url', coluna_alvo])
for col in colunas_numericas:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

# Sobrescreve salvando a base 100% higienizada com todas as propriedades preservadas
df.to_csv(caminho_bruto, index=False)

print(f"🏁 [T1] SUCESSO! Planilha de aprendizado limpa. Formato atual: {df.shape[1]} colunas estruturadas.")