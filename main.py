import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv() # carrega as variáveis do arquivo .env
chave = os.getenv("OPENAI_API_KEY")

# inicializa a ia apenas se a chave existir para evitar erros de autenticação
if not chave:
    st.error("Erro: OPENAI_API_KEY não encontrada no arquivo .env")
    st.stop()

modelo_ia = OpenAI(api_key=chave)  # inicializa a IA com a chave da API

st.write("# Chatbot com IA")  # formato markdown

if not "lista_mensagens" in st.session_state:  # se lista de msg existe/nao existe dentro dos cookies
    st.session_state["lista_mensagens"] = []   # cria lista vazia se nao tem msgs anteriores

# loop para exibir o histórico
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]  
    st.chat_message(role).write(content)  # mostra a msg na tela conforme o role

texto_user = st.chat_input("Digite sua mensagem")  # armazena a msg na variavel texte_user

if texto_user: 
    st.chat_message("user").write(texto_user)
    mensagem_user = {"role": "user", "content": texto_user}
    st.session_state["lista_mensagens"].append(mensagem_user)  # add a msg do user na lista de msgs

    # resposta da ia
    resposta_ia = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-4o",
    )
    texto_resposta_ia = resposta_ia.choices[0].message.content

    st.chat_message("assistant").write(texto_resposta_ia)
    mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)  # add a msg da ia na lista de msgs

