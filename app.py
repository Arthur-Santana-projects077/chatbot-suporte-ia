
import streamlit as st
import uuid
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory


# ==========================================
# CONFIGURAÇÕES INICIAIS
# ==========================================

load_dotenv()

st.set_page_config(
    page_title="Suporte IA",
    page_icon="💬",
    layout="centered"
)


# ==========================================
# CONFIGURAÇÃO DO CHATBOT
# ==========================================

@st.cache_resource
def configurar_chatbot():

    if not os.getenv("GROQ_API_KEY"):
        raise ValueError(
            "Chave GROQ_API_KEY não encontrada no arquivo .env."
        )

    llm = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0.7
    )

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

    chain = prompt | llm

    store = {}

    def get_session_history(session_id):

        if session_id not in store:
            store[session_id] = InMemoryChatMessageHistory()

        return store[session_id]

    chat = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="mensagem",
        history_messages_key="history"
    )

    return chat


# ==========================================
# INICIALIZAÇÃO DAS SESSÕES
# ==========================================

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []


# ==========================================
# BARRA LATERAL
# ==========================================

with st.sidebar:

    st.title("💬 Suporte IA")

    st.caption("Assistente virtual de atendimento")

    st.divider()

    if st.button("➕ Nova conversa", use_container_width=True):

        st.session_state.session_id = str(uuid.uuid4())
        st.session_state.messages = []

        st.rerun()

    if st.button("🗑️ Limpar conversa", use_container_width=True):

        st.session_state.messages = []
        st.session_state.session_id = str(uuid.uuid4())

        st.rerun()

    st.divider()

    st.markdown("### Sobre o aplicativo")

    st.write("Assistente virtual desenvolvido com:")

    st.markdown("""
    - Python
    - Streamlit
    - LangChain
    - Groq API
    """)

    st.divider()

    st.caption("Projeto de chatbot de suporte ao cliente")


# ==========================================
# INTERFACE PRINCIPAL
# ==========================================

st.title("💬 Assistente de Suporte")

st.write(
    "Olá! Sou seu assistente virtual. "
    "Como posso ajudar você hoje?"
)

st.divider()


# ==========================================
# CARREGAR HISTÓRICO NA TELA
# ==========================================

for mensagem in st.session_state.messages:

    with st.chat_message(mensagem["role"]):

        st.markdown(mensagem["content"])


# ==========================================
# CAMPO DE ENVIO DE MENSAGENS
# ==========================================

mensagem_usuario = st.chat_input(
    "Digite sua mensagem..."
)


# ==========================================
# PROCESSAMENTO DA CONVERSA
# ==========================================

if mensagem_usuario:

    # Exibir mensagem do usuário
    st.session_state.messages.append({
        "role": "user",
        "content": mensagem_usuario
    })

    with st.chat_message("user"):
        st.markdown(mensagem_usuario)

    # Gerar resposta da IA
    with st.chat_message("assistant"):

        with st.spinner("Pensando..."):

            try:

                chat = configurar_chatbot()

                result = chat.invoke(
                    {"mensagem": mensagem_usuario},
                    config={
                        "configurable": {
                            "session_id": st.session_state.session_id
                        }
                    }
                )

                resposta = result.content

                st.markdown(resposta)

                # Salvar resposta no histórico visual
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": resposta
                })

            except Exception as erro:

                st.error(
                    f"Não foi possível obter uma resposta: {erro}"
                )

                st.info(
                    "Verifique sua conexão e tente novamente."
                )
