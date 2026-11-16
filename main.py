
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# Carregar variáveis de ambiente
load_dotenv()

# Conectar ao modelo Groq
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.7
)

# Criar o prompt com histórico de conversação
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        Você é um assistente virtual de suporte ao cliente.

        Responda sempre em português brasileiro.
        Seja educado, objetivo e prestativo.
        Ajude o cliente a resolver seus problemas.
        Utilize o histórico da conversa para manter o contexto.
        """
    ),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{mensagem}")
])

# Criar a cadeia
chain = prompt | llm

# Armazenar históricos das sessões
store = {}


def get_session_history(session_id):

    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()

    return store[session_id]


# Adicionar memória ao chatbot
chat = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="mensagem",
    history_messages_key="history"
)

# Identificador da conversa
session_id = "session1"

print("================================")
print(" CHATBOT DE SUPORTE AO CLIENTE")
print("================================")
print("Digite 'sair' para encerrar.")

# Iniciar conversa
while True:

    mensagem = input("Você: ")

    if mensagem.lower() == "sair":
        print("Chatbot: Até logo!")
        break

    try:

        result = chat.invoke(
            {"mensagem": mensagem},
            config={
                "configurable": {
                    "session_id": session_id
                }
            }
        )

        print("Chatbot:", result.content)

    except Exception as erro:
        print("Erro ao executar:", erro)
