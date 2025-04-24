import fitz  # PyMuPDF

def extract_text_from_pdf(path):
    texto = ""  # Variável para armazenar o texto extraído
    with fitz.open(path) as pdf:  # Abre o arquivo PDF
        for page in pdf:  # Percorre todas as páginas do PDF
            texto += page.get_text()  # Extrai o texto da página
    return texto.strip()  # Retorna o texto limpo, sem espaços extras
 
