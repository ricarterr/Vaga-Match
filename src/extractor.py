import fitz  # PyMuPDF
import re
from unidecode import unidecode

def extrair_texto_pdf(caminho_arquivo):
    try:
        with fitz.open(caminho_arquivo) as doc:
            texto = ""
            for pagina in doc:
                texto += pagina.get_text()
    except Exception as e:
        print("Erro ao abrir o PDF:", e)
        return ""

    texto = corrigir_texto_bugado(texto)
    return texto

def corrigir_texto_bugado(texto):
    texto = re.sub(r'\s+', ' ', texto)  # remove espaços extras
    texto = unidecode(texto)  # remove acentos
    texto = texto.replace('7elefone', 'Telefone')  # exemplo de correção
    texto = re.sub(r'[^\w\s.,:;!?()\-+@]', '', texto)  # remove caracteres bugados
    return texto.strip()
