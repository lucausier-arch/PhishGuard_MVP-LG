# -*- coding: utf-8 -*-
"""
🎲 GERADOR DE LOTE CEGO ALEATÓRIO — criar_lote_teste.py
LG Electronics AX Academy | João Lucas Mota Ausier
"""

import os
import pandas as pd
import random

# Força a reprodutibilidade da mistura aleatória
random.seed(42)

PASTA_DATA = "data"
os.makedirs(PASTA_DATA, exist_ok=True)

# 🟢 50 URLs Legítimas (Target = 0)
legitimos = [
    ("https://www.lg.com", 0), ("https://www.google.com", 0), ("https://www.microsoft.com", 0),
    ("https://www.amazon.com.br", 0), ("https://www.apple.com/br", 0), ("https://www.netflix.com", 0),
    ("https://www.github.com", 0), ("https://www.linkedin.com", 0), ("https://www.youtube.com", 0),
    ("https://www.wikipedia.org", 0), ("https://www.globo.com", 0), ("https://www.uol.com.br", 0),
    ("https://www.estadao.com.br", 0), ("https://www.mercadolivre.com.br", 0), ("https://www.magazineluiza.com.br", 0),
    ("https://www.casasbahia.com.br", 0), ("https://www.americanas.com.br", 0), ("https://www.samsung.com/br", 0),
    ("https://www.sony.com.br", 0), ("https://www.dell.com/pt-br", 0), ("https://www.hp.com/br-pt", 0),
    ("https://www.intel.com.br", 0), ("https://www.oracle.com/br", 0), ("https://www.ibm.com/br-pt", 0),
    ("https://www.adobe.com/br", 0), ("https://www.salesforce.com/br", 0), ("https://www.cisco.com/c/pt_br", 0),
    ("https://www.zoom.us", 0), ("https://www.spotify.com/br", 0), ("https://www.instagram.com", 0),
    ("https://www.facebook.com", 0), ("https://www.itau.com.br", 0), ("https://www.bancodobrasil.com.br", 0),
    ("https://www.caixa.gov.br", 0), ("https://www.bradesco.com.br", 0), ("https://www.santander.com.br", 0),
    ("https://www.nubank.com.br", 0), ("https://www.inter.co", 0), ("https://www.btgpactual.com", 0),
    ("https://www.accenture.com/br-pt", 0), ("https://www.deloitte.com/br", 0), ("https://www.pwc.com.br", 0),
    ("https://www.ey.com/pt_br", 0), ("https://www.gov.br", 0), ("https://www.receita.fazenda.gov.br", 0),
    ("https://www.correios.com.br", 0), ("https://www.serasa.com.br", 0), ("https://www.sp.gov.br", 0),
    ("https://www.rio.rj.gov.br", 0), ("https://www.g1.globo.com", 0)
]

# 🚨 50 URLs de Phishing Simuladas (Target = 1)
phishing = [
    ("http://www.lg-electronics-verificacao.com/login", 1), ("http://www.suporte-lg-manaus.net/atualizacao", 1),
    ("http://www.lg-promocao-smarttv.com.br/cadastrar", 1), ("http://login.lg-account-security.com/auth", 1),
    ("http://www.lgg-electronics.com/br", 1), ("http://www.g00gle-security-panel.com", 1),
    ("http://www.accounts-google-com-login.net", 1), ("http://www.micros0ft-update-service.com", 1),
    ("http://www.login-microsoft-office365.online", 1), ("http://www.amazon-br-promocoes.com/ofertas", 1),
    ("http://www.verificar-conta-amazon.tech", 1), ("http://www.netfl1x-cancelamento.com/recadastro", 1),
    ("http://www.netflix-assistência-cliente.store", 1), ("http://www.githuub-security-alerts.com", 1),
    ("http://www.linkedin-vagas-corporativas.info", 1), ("http://www.visualizar-comprovante-pdf.cc", 1),
    ("http://www.mercadolivre-compra-retida.site", 1), ("http://www.mercadol1vre-seguranca.com/dispositivo", 1),
    ("http://www.magazine-luiza-precos-baixos.online", 1), ("http://www.casasbahia-limpa-estoque.com", 1),
    ("http://www.americanas-cupons-desconto.tech", 1), ("http://www.samsung-recrutamento-ax.com", 1),
    ("http://www.nubank-atualiza-cadastro.com/token", 1), ("http://www.nu-limite-imediato.site/promocao", 1),
    ("http://www.itau-seguranca-corporativa.net", 1), ("http://www.itaucard-sincronizar-token.org", 1),
    ("http://.bradesco-net-empresa-validacao.com", 1), ("http://www.bancodobrasil-central-atendimento.info", 1),
    ("http://www.caixa-auxilio-poupanca.online", 1), ("http://www.santander-empresarial-login.top", 1),
    ("http://www.banco-inter-atualizacao-obrigatoria.com", 1), ("http://www.recadastramento-gov-br.xyz", 1),
    ("http://www.consulta-cpf-receita-federal.club", 1), ("http://www.correios-rastreamento-taxado.com", 1),
    ("http://www.serasa-limpa-nome-score.biz", 1), ("http://www.facebook-security-check-login.com", 1),
    ("http://www.instagram-verify-badge.co/apply", 1), ("http://www.suporte-tecnico-ti-corporativo.net", 1),
    ("http://www.faturamento-lg-eletronics.com", 1), ("http://www.g1-noticias-urgente-manaus.com", 1),
    ("http://www.uol-noticias-exclusivas.online", 1), ("http://www.valida-credencial-lg.com/colaborador", 1),
    ("http://www.webmail-lg-manufatura.net/roundcube", 1), ("http://www.security-update-windows11.info", 1),
    ("http://www.paypal-dispute-resolution.tech", 1), ("http://www.dhl-entrega-pendente.com/rastreio", 1),
    ("http://www.fedex-package-delivery-status.com", 1), ("http://www.apple-id-cloud-verification.com", 1),
    ("http://www.icloud-find-my-iphone-login.net", 1), ("http://www.cloud-storage-shared-file.download", 1)
]

# Une as duas listas
lista_completa = legitimos + phishing

# Executa o embaralhamento estatístico puro
random.shuffle(lista_completa)

# Transforma em DataFrame
df_banca = pd.DataFrame(lista_completa, columns=["url", "target"])

# Salva diretamente na pasta correta do projeto
caminho_final = os.path.join(PASTA_DATA, "dataset2_banca.csv")
df_banca.to_csv(caminho_final, index=False, encoding="utf-8")

print(f"🎲 Sucesso! Arquivo '{caminho_final}' gerado com 100 links redistribuídos aleatoriamente.")
print(f"   ↳ Proporção: {df_banca[df_banca['target'] == 0].shape[0]} Legítimos | {df_banca[df_banca['target'] == 1].shape[0]} Phishing.")