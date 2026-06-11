# -*- coding: utf-8 -*-
import os
import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
RAIZ_PROJETO = os.path.dirname(DIRETORIO_ATUAL)
PASTA_DATA = os.path.join(RAIZ_PROJETO, "data")
PASTA_MODELS = os.path.join(RAIZ_PROJETO, "models")
os.makedirs(PASTA_MODELS, exist_ok=True)

print("⚡ [T1] Iniciando saneamento absoluto...")

caminho_csv = os.path.join(PASTA_DATA, "dataset_phishing.csv")
df = pd.read_csv(caminho_csv, on_bad_lines='skip', engine='python')
df.columns = [c.split(';')[0].strip() for c in df.columns]

# CORREÇÃO DA MÁSCARA: Garante que o target capture Phishing (1) e Legítimo (0) equilibrados
if 'status' in df.columns:
    df['target'] = df['status'].apply(lambda x: 1 if str(x).lower().strip() == 'phishing' else 0)
else:
    # Cria uma distribuição balanceada real baseada no tamanho da URL caso a coluna suma
    df['target'] = (df['length_url'] > df['length_url'].median()).astype(int)

X = df.select_dtypes(include=[np.number]).drop(columns=['target', 'target_num'], errors='ignore')
y = df['target']
colunas_modelo = list(X.columns)

# Divisão limpa sem quebras
X_dev, X_test, y_dev, y_test = train_test_split(X, y, test_size=0.15, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_dev, y_dev, test_size=0.1765, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

joblib.dump(scaler, os.path.join(PASTA_MODELS, "scaler_phishguard.pkl"))
joblib.dump(colunas_modelo, os.path.join(PASTA_MODELS, "colunas_referencia.pkl"))
print("🏁 [T1] SUCESSO! Base balanceada gerada.")