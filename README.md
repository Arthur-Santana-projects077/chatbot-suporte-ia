
# 💬 Chatbot de Suporte IA

Chatbot inteligente de atendimento ao cliente desenvolvido em Python, utilizando LangChain, Streamlit e Groq API.

## 🚀 Funcionalidades

- Chat interativo para atendimento ao cliente.
- Memória de conversação por sessão.
- Contextualização das respostas com base no histórico.
- Criação de novas conversas.
- Limpeza do histórico de mensagens.
- Interface desenvolvida com Streamlit.

## 🛠️ Tecnologias utilizadas

- Python
- Streamlit
- LangChain
- Groq API
- GPT-OSS 20B
- Python-dotenv

## ⚙️ Como executar o projeto

Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/chatbot-suporte-ia.git
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

Instale as dependências:

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

## 🔐 Segurança

A chave da API deve permanecer no arquivo `.env`, que não deve ser publicado no GitHub.

## 🔮 Melhorias futuras

- Integração com banco de dados PostgreSQL.
- Implementação de RAG para consulta a documentos.
- Classificação automática de chamados.
- Integração com dashboards e Power BI.

## 👨‍💻 Autor

Arthur Santana
