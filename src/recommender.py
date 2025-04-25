from fuzzywuzzy import fuzz

palavras_chave = [
    "Python", "Java", "SQL", "Machine Learning", "Deep Learning",
    "Estatística", "Data Science", "Análise de Dados", "Engenharia",
    "Desenvolvedor", "C++", "Javascript", "AI"
]

def encontrar_palavras_chave(texto, limiar=80):
    texto = texto.lower()
    palavras_encontradas = []

    for palavra in palavras_chave:
        score = fuzz.partial_ratio(palavra.lower(), texto)
        if score >= limiar:
            palavras_encontradas.append(palavra)

    return palavras_encontradas

