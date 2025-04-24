import os
import re
from PyPDF2 import PdfReader
from fuzzywuzzy import fuzz

# Lista de palavras-chave que queremos detectar
palavras_chave = [
    "Python", "Java", "JavaScript", "Machine Learning", "Data Science", "SQL",
    "IA", "AI", "Deep Learning", "Engenharia", "Desenvolvedor", "Análise de Dados",
    "Informática", "Tecnologias", "Estatística", "Big Data", "Segurança da Informação"
]

# Lista de correções manuais para palavras bugadas
correcoes = {
    "QIRUPiWLFD": "Informática",
    "THFQRORJLDV": "Tecnologias",
    "3URMHWR": "Projeto",
    "SIRIWZDUH": "Software",
    "0DFKLQH": "Machine",
    "/(DUQLQJ": "Learning",
    "VWDWtVWLFD": "Estatística",
    "DQDOLVH": "Análise",
    "GDGRV": "Dados",
    "GHVHQYROYLPHQWR": "Desenvolvimento",
    "JLO": "Ágil",
    "ELJ": "Big",
    "GDWD": "Data"
}

def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ''
        for page in reader.pages:
            text += page.extract_text() or ''
        print("Texto extraído com sucesso!\n")
        return text
    except Exception as e:
        print("Erro ao abrir o PDF:", e)
        return ''

def corrigir_texto_bugado(texto):
    # Remove caracteres não ASCII como ♥
    texto = re.sub(r'[^\x00-\x7F]+', '', texto)

    # Aplica correções manuais
    for errado, certo in correcoes.items():
        texto = texto.replace(errado, certo)

    return texto

def buscar_palavras_chave(texto, palavras_chave, limite_fuzzy=80):
    encontradas = []
    for palavra in palavras_chave:
        for palavra_do_texto in texto.split():
            similaridade = fuzz.partial_ratio(palavra.lower(), palavra_do_texto.lower())
            if similaridade >= limite_fuzzy:
                encontradas.append(palavra)
                break
    return list(set(encontradas))

if __name__ == '__main__':
    # Caminho do currículo
    pdf_path = os.path.join("data", "meu_curriculo.pdf")  # Corrija esse nome se for diferente

    texto_extraido = extract_text_from_pdf(pdf_path)
    texto_corrigido = corrigir_texto_bugado(texto_extraido)

    print("Texto limpo:\n", texto_corrigido, "\n")

    palavras_encontradas = buscar_palavras_chave(texto_corrigido, palavras_chave)
    print("Palavras-chave encontradas no currículo:")
    print(palavras_encontradas if palavras_encontradas else "Nenhuma palavra-chave encontrada.")
