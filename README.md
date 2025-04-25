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
