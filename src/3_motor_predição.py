# -*- coding: utf-8 -*-
"""
🛡️ TRABALHO 3: MOTOR REATIVO DO GATEWAY DE INFRAESTRUTURA DE REDES
LG Electronics Security Team | Proteção Ativa Contra Typosquatting
"""

import os
import joblib
import pandas as pd
from urllib.parse import urlparse

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
RAIZ_PROJETO = os.path.dirname(DIRETORIO_ATUAL)
PASTA_MODELS = os.path.join(RAIZ_PROJETO, "models")

class GatewayBordaMle:
    def __init__(self):
        caminho_modelo = os.path.join(PASTA_MODELS, "best_model_phishguard.pkl")
        caminho_scaler = os.path.join(PASTA_MODELS, "scaler_phishguard.pkl")
        caminho_colunas = os.path.join(PASTA_MODELS, "colunas_referencia.pkl")
        
        self.modelo = joblib.load(caminho_modelo)
        self.scaler = joblib.load(caminho_scaler)
        self.colunas = joblib.load(caminho_colunas)
        self.threshold = 0.35

    def extrair_atributos_ao_vivo(self, url_bruta):
        url = str(url_bruta).strip().lower()
        if not url.startswith(('http://', 'https://')):
            url_analise = 'http://' + url
        else:
            url_analise = url
            
        parsed = urlparse(url_analise)
        netloc = parsed.netloc
        
        # Mapeamento básico estrutural
        atributos = {col: 0 for col in self.colunas}
        atributos['length_url'] = len(url)
        atributos['length_hostname'] = len(netloc)
        atributos['nb_dots'] = url.count('.')
        atributos['nb_hyphens'] = url.count('-')
        atributos['nb_at'] = url.count('@')
        atributos['nb_slash'] = url.count('/')
        atributos['nb_www'] = 1 if 'www.' in url else 0
        atributos['https_token'] = 1 if url_bruta.startswith('https') else 0
        
        return pd.DataFrame([atributos])[self.colunas]

    def analisar_link(self, url_bruta):
        url_limpa = str(url_bruta).strip()
        
        # REGRA DE OURO ATIVA (Heurística de Proteção Industrial contra Typosquatting)
        # Se o link contiver variações visuais falsas de marcas protegidas, força o risco para 100%
        gatilhos_fraude = ['googie', 'go0gle', 'suporte-lg', 'lg-verificacao', 'lgg-', 'micros0ft', 'netfl1x', 'mercadol1vre']
        
        contem_fraude_visual = any(gatilho in url_limpa.lower() for gatilho in gatilhos_fraude)
        
        # Adiciona verificação específica para o 'googIe' (com I maiúsculo)
        if "googIe" in url_limpa or contem_fraude_visual:
            probabilidade_phishing = 1.0  # Risco Máximo Forçado por Política de Segurança
            veridito = "🚫 BLOQUEADO (Ameaça de Typosquatting Interceptada)"
            classe = 1
            return probabilidade_phishing, veridito, classe
            
        # Caso não caia na regra de ouro, roda o modelo de Machine Learning normal
        vetor_recursos = self.extrair_atributos_ao_vivo(url_bruta)
        vetor_scaled = self.scaler.transform(vetor_recursos)
        probabilidade_phishing = self.modelo.predict_proba(vetor_scaled)[0, 1]
        
        if probabilidade_phishing >= self.threshold:
            veridito = "🚫 BLOQUEADO (Ameaça Preventiva Interceptada na Borda)"
            classe = 1
        else:
            veridito = "🟢 LIBERADO (Tráfego Seguro Autorizado)"
            classe = 0
            
        return probabilidade_phishing, veridito, classe