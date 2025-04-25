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

# Entre no diretório do projeto
cd Vaga-Match

# Instale as dependências
pip install -r requirements.txt

# Execute o analisador (exemplo)
python src/analyzer.py

```
## 🧱 Estrutura básica de pastas

```text
vaga-match/
│
├── data/                  # Currículos e vagas (PDFs, .txt) - Exemplo, ajuste conforme necessário
│
├── src/                   # Código-fonte
│   ├── extractor.py       # Leitura e correção do texto
│   ├── analyzer.py        # Analisador de currículo x vaga
│   └── recommender.py     # Sugestão de melhorias
│
├── requirements.txt       # Lista de dependências
├── LICENSE.md             # Termos da licença não-comercial
├── README.md              # Apresentação do projeto
└── .gitignore             # Ignorar arquivos indesejados


⚠️ Licenciamento Importante ⚠️
Este projeto opera sob um modelo de licenciamento duplo:
Uso Pessoal / Não Comercial:
Gratuito para uso pessoal, educacional ou por organizações sem fins lucrativos.
Requer atribuição (créditos) ao autor original (Pedro Ricarte).
Proíbe a venda do software.
Consulte o arquivo LICENSE.md para os termos completos da licença não comercial.
Uso Comercial:
Qualquer uso por empresas, para fins lucrativos, em ambiente de negócios, ou incorporação em produtos/serviços comerciais requer uma licença comercial paga.
A licença comercial também exige atribuição (créditos).
Entre em contato com: pedrorcrt12@gmail.com

Ao usar este software, você concorda com os termos de licenciamento aplicáveis.

✍️ Autor
Desenvolvido por Pedro Ricarte
GitHub: @ricarterr 
