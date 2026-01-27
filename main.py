# titulo
# input
# a cada msg do user:
    # mostra a msg que ele enviou
    # pega msg e envia para uma IA responder
    # exibir a msg da IA na tela


import streamlit as st

st.write("# Chatbot com IA")  # formato markdown

if not "lista_mensagens" in st.session_state:  # se lista de msg existe/nao existe dentro dos cookies
    st.session_state["lista_mensagens"] = []   # cria uma lista vazia se nao tem msg anteriores, se já existe nao faz nada

texto_user = st.chat_input("Digite sua mensagem")  # armazena a msg na variavel texte_user

for mensagem in st.session_state["lista_mensagens"]:  # para cada msg na lista de msg armazenadas
    role = mensagem["role"]
    content = mensagem["content"]  
    st.chat_message(role).write(content)  # mostra a msg na tela conforme o role (user/assistant/system)

if texto_user: 
   st.chat_message("user").write(texto_user)
   mensagem_user = {"role": "user", "content": texto_user}
   st.session_state["lista_mensagens"].append(mensagem_user)  # adiciona a msg do user na lista de msgs

   resposta_ia = "Você disse: " + texto_user # concatenação simples de 2 textos

   st.chat_message("assistant").write(resposta_ia)
   mensagem_ia = {"role": "assistant", "content": resposta_ia}
   st.session_state["lista_mensagens"].append(mensagem_ia)  # adiciona a msg da ia na lista de msgs


   #Anotações

# visualizar o sistema: streamlit run main.py 

   # pip install streamlit openai
   # principais ferramentas na criação de sistemas py:
      # Streamlit - para criar a interface web, apenas com python cria o front e o back (em markdown)
      # Flask - para criar APIs, microframework leve, dinamico e flexível
      # Django - para criar aplicações web completas, já vem com várias funcionalidades prontas
      # FastAPI - para criar APIs rápidas e performáticas, obriga a estruturar o projeto de 1 maneira
   # posso usar essa ia no meu site para falar com os usuarios, responder perguntas sobre os produtos, empresa, etc
   # st.chat_message("user").write() aparece a msg com icone de usuario
   # st.chat_message("assistant").write() aparece a msg com icone de robo
   # st.chat_message("Manu").write() aparece com a letra inicial do usuario
   # st.session_state: cookies do navegador para armazenar dados temporarios, já existe a lista de msg?
   # print(st.session_state["lista_mensagens"]) mostra no terminal do streamlit todas as msgs armazenadas
   # Hugging Face - plataforma de modelos de IA, hospeda modelos de ML, datasets e apps de IA sem usar o openai
   # Gradio - biblioteca para criar interfaces web para modelos de ML, fácil de usar e integrar

