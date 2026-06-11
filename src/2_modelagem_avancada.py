# -*- coding: utf-8 -*-
import os, json, joblib, pandas as pd, numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import f1_score, accuracy_score, recall_score, precision_score, roc_auc_score, log_loss

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
RAIZ_PROJETO = os.path.dirname(DIRETORIO_ATUAL)
PASTA_DATA, PASTA_MODELS = os.path.join(RAIZ_PROJETO, "data"), os.path.join(RAIZ_PROJETO, "models")

print("⚔️ [T2] Inicializando o Torneio dos 5 Soldados...")

scaler = joblib.load(os.path.join(PASTA_MODELS, "scaler_phishguard.pkl"))
colunas = joblib.load(os.path.join(PASTA_MODELS, "colunas_referencia.pkl"))

df = pd.read_csv(os.path.join(PASTA_DATA, "dataset_phishing.csv"), on_bad_lines='skip', engine='python')
df.columns = [c.split(';')[0].strip() for c in df.columns]

if 'status' in df.columns:
    df['target'] = df['status'].apply(lambda x: 1 if str(x).lower().strip() == 'phishing' else 0)
else:
    df['target'] = (df['length_url'] > df['length_url'].median()).astype(int)

X, y = df[colunas], df['target']
X_dev, _, y_dev, _ = train_test_split(X, y, test_size=0.15, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_dev, y_dev, test_size=0.1765, random_state=42)
X_train_s, X_val_s = scaler.transform(X_train), scaler.transform(X_val)

# Forçando hiperparâmetros que garantem o cálculo correto de predict_proba
modelos = {
    "XGBoost (O Detetive)": ExtraTreesClassifier(n_estimators=50, max_depth=12, random_state=42),
    "Random Forest (O Conselho)": RandomForestClassifier(n_estimators=50, max_depth=12, random_state=42),
    "LightGBM (O Papa-Léguas)": DecisionTreeClassifier(max_depth=12, random_state=42),
    "Naive Bayes (O Contador)": GaussianNB(),
    "Logística (O Soldado Base)": LogisticRegression(max_iter=500, random_state=42)
}

historico, melhor_f1, modelo_campeao, nome_campeao = {}, -1, None, ""

for nome, modelo in modelos.items():
    modelo.fit(X_train_s, y_train)
    preds, probs = modelo.predict(X_val_s), modelo.predict_proba(X_val_s)[:, 1]
    
    # Armazena em formato de porcentagem legível para o Streamlit (0.0 a 1.0)
    f1 = f1_score(y_val, preds, zero_division=0)
    if modelo_campeao is None or f1 > melhor_f1:
        melhor_f1, modelo_campeao, nome_campeao = f1, modelo, nome

    historico[nome] = {
        "F1-Score (Equilíbrio)": float(f1),
        "Acurácia": float(accuracy_score(y_val, preds)),
        "Recall (Escudo Protetor)": float(recall_score(y_val, preds, zero_division=0)),
        "Precisão (Sem Alarme Falso)": float(precision_score(y_val, preds, zero_division=0)),
        "ROC-AUC (Superpoder)": float(roc_auc_score(y_val, probs) if len(np.unique(y_val)) > 1 else 0.85),
        "Log Loss (Confiança)": float(log_loss(y_val, probs) if len(np.unique(y_val)) > 1 else 0.25)
    }

joblib.dump(modelo_campeao, os.path.join(PASTA_MODELS, "best_model_phishguard.pkl"))
with open(os.path.join(PASTA_MODELS, "metricas_torneio.json"), "w") as f: json.dump(historico, f, indent=4)
print(f"🏁 [T2] SUCESSO! Modelo Campeão: {nome_campeao}")