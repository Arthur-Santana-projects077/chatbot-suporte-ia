
# ðŸ’¬ Chatbot de Suporte IA

Chatbot inteligente de atendimento ao cliente desenvolvido em Python, utilizando LangChain, Streamlit e Groq API.

## ðŸš€ Funcionalidades

- Chat interativo para atendimento ao cliente.
- MemÃ³ria de conversaÃ§Ã£o por sessÃ£o.
- ContextualizaÃ§Ã£o das respostas com base no histÃ³rico.
- CriaÃ§Ã£o de novas conversas.
- Limpeza do histÃ³rico de mensagens.
- Interface desenvolvida com Streamlit.

## ðŸ› ï¸ Tecnologias utilizadas

- Python
- Streamlit
- LangChain
- Groq API
- GPT-OSS 20B
- Python-dotenv

## âš™ï¸ Como executar o projeto

Clone o repositÃ³rio:

```bash
git clone https://github.com/Arthur-Santana-projects077/chatbot-suporte-ia.git
```

Entre na pasta:

```bash
cd chatbot-suporte-ia
```

Crie e ative o ambiente virtual:

```bash
python -m venv venv
```

No Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Instale as dependÃªncias:

```bash
pip install -r requirements.txt
```

Configure sua chave da Groq em um arquivo `.env`:

```env
GROQ_API_KEY=sua_chave_aqui
```

Execute o aplicativo:

```bash
streamlit run app.py
```

## ðŸ” SeguranÃ§a

A chave da API deve permanecer no arquivo `.env`, que nÃ£o deve ser publicado no GitHub.

## ðŸ”® Melhorias futuras

- IntegraÃ§Ã£o com banco de dados PostgreSQL.
- ImplementaÃ§Ã£o de RAG para consulta a documentos.
- ClassificaÃ§Ã£o automÃ¡tica de chamados.
- IntegraÃ§Ã£o com dashboards e Power BI.

## ðŸ‘¨â€ðŸ’» Autor

Arthur Santana

