# -*- coding: utf-8 -*-
"""
🛡️ MVP PHISHGUARD - MOTOR DE INFERÊNCIA HÍBRIDO INTEGRADO
LG Electronics Security Team | Execução Dinâmica sobre Dados Devolvidos
"""

import os
import pickle
import warnings
import pandas as pd
import numpy as np
from scipy.sparse import hstack

warnings.filterwarnings("ignore")

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
RAIZ_PROJETO = os.path.dirname(DIRETORIO_ATUAL)
PASTA_DATA = os.path.join(RAIZ_PROJETO, "data")
PASTA_MODELS = os.path.join(RAIZ_PROJETO, "models")

def executar_predicao_fluxo():
    print("🚀 [Back-end] Iniciando inferência combinada sobre os dados devolvidos...")
    
    caminho_cego = os.path.join(PASTA_DATA, "dataset_2_execucao_cego.csv")
    caminho_pkl = os.path.join(PASTA_MODELS, "comite_5_modelos.pkl")
    
    if not os.path.exists(caminho_cego) or not os.path.exists(caminho_pkl):
        print("⚠️ Erro crítico: Certifique-se de que o arquivo comite_5_modelos.pkl e o dataset_2 estão nas pastas corretas.")
        return

    df_cego = pd.read_csv(caminho_cego)
    df_cego.columns = [str(c).strip().lower() for c in df_cego.columns]
    
    coluna_url = 'url' if 'url' in df_cego.columns else df_cego.columns[0]
    
    with open(caminho_pkl, 'rb') as f:
        comite = pickle.load(f)
        
    vectorizer = comite['vectorizer']
    colunas_numericas_exigidas = comite['colunas_numericas']
    
    print("🧠 [Back-end] Processando cadeias de strings e lendo colunas numéricas devolvidas...")
    X_texto = df_cego[coluna_url].astype(str).tolist()
    X_texto_vetorizado = vectorizer.transform(X_texto)
    
    # Garante que todas as colunas exigidas pelo modelo híbrido existam
    for col in colunas_numericas_exigidas:
        if col not in df_cego.columns:
            df_cego[col] = 0.0
            
    X_num_devolvido = df_cego[colunas_numericas_exigidas].astype(float).values
    
    # Une as duas matrizes (Texto + Números)
    X_combinado = hstack([X_texto_vetorizado, X_num_devolvido]).toarray()
    
    # Executa a predição real pelo modelo pioneiro
    probabilidades = comite['Random Forest'].predict_proba(X_combinado)[:, 1]
    
    df_resultado = pd.DataFrame()
    df_resultado['url'] = df_cego[coluna_url]
    df_resultado['probabilidade_phishing'] = probabilidades
    df_resultado['veredito'] = np.where(probabilidades >= 0.50, 'Phishing', 'Veridico')
    
    output_banco = os.path.join(PASTA_DATA, "historico_analisado_gateway.csv")
    df_resultado.to_csv(output_banco, index=False)
    print(f"🏁 [SUCESSO] Inferência Concluída! Resultado salvo em: {output_banco}")

if __name__ == "__main__":
    executar_predicao_fluxo()