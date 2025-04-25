from src.extractor import extrair_texto_pdf
from src.recommender import encontrar_palavras_chave

arquivo_pdf = 'data/meu_curriculo.pdf'

texto = extrair_texto_pdf(arquivo_pdf)

print("\nTexto limpo:")
print(texto)

palavras = encontrar_palavras_chave(texto)

if palavras:
    print("\nPalavras-chave encontradas no currículo:")
    print(palavras)
else:
    print("\nNenhuma palavra-chave encontrada.")
 
