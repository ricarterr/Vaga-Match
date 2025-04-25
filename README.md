# 🤖 Vaga-Match - Analisador Inteligente de Currículos

Projeto em Python que analisa currículos e compara automaticamente com vagas de emprego, mesmo quando o texto dos currículos está corrompido (PDF com fontes bugadas, etc).  
Também sugere melhorias no currículo com base na vaga.

---

## 🚀 Funcionalidades

- ✅ Extração de texto mesmo com fontes quebradas
- 🧠 Correção automática de palavras bugadas
- 🔍 Fuzzy Matching para identificar palavras-chave da vaga no currículo
- 📊 Sugestões de melhoria personalizadas

---

## 🛠️ Tecnologias Usadas

- Python
- PyMuPDF
- FuzzyWuzzy
- Unidecode
- Regex

---

## 📂 Como usar

```bash
# Clone o projeto
git clone https://github.com/ricarterr/Vaga-Match.git

# Instale as dependências
pip install -r requirements.txt

# Execute o analisador
python src/analyzer.py


🧱 Estrutura básica de pastas

vaga-match/
│
├── data/                  # Currículos e vagas (PDFs, .txt)
│
├── src/                   # Código-fonte
│   ├── extractor.py       # Leitura e correção do texto
│   ├── analyzer.py        # Analisador de currículo x vaga
│   └── recommender.py     # Sugestão de melhorias
│
├── requirements.txt       # Lista de dependências
├── README.md              # Apresentação do projeto
└── .gitignore             # Ignorar arquivos indesejados (explicado abaixo)


✍️ Autor
Desenvolvido por Pedro Ricarte
GitHub: @ricarterr
