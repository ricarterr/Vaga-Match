import os
import re
from PyPDF2 import PdfReader
from fuzzywuzzy import fuzz
from collections import Counter

# Função para extrair texto do PDF
def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ''
        for page in reader.pages:
            text += page.extract_text() or ''
        return text
    except Exception as e:
        print("Erro ao abrir o PDF:", e)
        return ''

# Função para corrigir texto com problemas de codificação
def corrigir_texto_bugado(texto):
    texto = re.sub(r'[^\x00-\x7F]+', '', texto)  # Remove caracteres não ASCII
    return texto

# Função para encontrar termos mais relevantes (sem lista fixa)
def buscar_termos_relevantes(texto, top_n=15):
    # Filtra palavras com mais de 3 letras e remove stopwords simples
    palavras = re.findall(r'\b\w{4,}\b', texto.lower())
    stopwords = {"para", "com", "que", "uma", "dos", "das"}
    palavras_filtradas = [p for p in palavras if p not in stopwords]
    
    # Contagem de frequência e seleção dos termos mais comuns
    contador = Counter(palavras_filtradas)
    return [termo.capitalize() for termo, _ in contador.most_common(top_n)]

if __name__ == '__main__':
    pdf_path = os.path.join("data", "meu_curriculo.pdf")
    texto_extraido = extract_text_from_pdf(pdf_path)
    texto_corrigido = corrigir_texto_bugado(texto_extraido)
    
    termos_relevantes = buscar_termos_relevantes(texto_corrigido)
    print("Termos mais relevantes encontrados:")
    print(termos_relevantes if termos_relevantes else "Nenhum termo relevante.")
