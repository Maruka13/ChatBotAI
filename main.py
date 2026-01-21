# titulo
# input
# a cada msg do user:
    # mostra a msg que ele enviou
    # pega msg e envia para uma IA responder
    # exibir a msg da IA na tela

#Anotações
   # pip install streamlit openai
   # principais ferramentas na criação de sistemas py:
      # Streamlit - para criar a interface web, apenas com python cria o front e o back (em markdown)
      # Flask - para criar APIs, microframework leve, dinamico e flexível
      # Django - para criar aplicações web completas, já vem com várias funcionalidades prontas
      # FastAPI - para criar APIs rápidas e performáticas, obriga a estruturar o projeto de 1 maneira
   # visualizar o sistema: streamlit run main.py 

import streamlit as st

st.write("# Chatbot com IA")  # formato markdown

texto_user = st.chat_input("Digite sua mensagem")  # armazena a msg na variavel texte_user

if texto_user: 
    print(texto_user)