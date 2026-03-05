# titulo
# input
# a cada msg do user:
    # mostra a msg que ele enviou
    # pega msg e envia para uma IA responder
    # exibir a msg da IA na tela


# listas

# listas sao feitas entre colchetes []
# armazena apenas um tipo de dado por lista

lista_nova = [] # lista vazia
nomes = ["Manu", "Cris", "Alvaro", "Rennan"]
print(nomes[0])  # acessa o primeiro item da lista

nomes.append("Isa")  # .append adiciona um item no final da lista
print(nomes)


# dicionario

# dicionarios sao feitos com chaves {chave: valor, chave: valor}
# armazena varias informações por item

idades = {"Manu": 25, "Cris": 54, "Alvaro": 12, "Rennan": 24}
print(idades["Manu"])  # pega info no dicionario -> dicionario[chave]
idades["Isa"] = 23  # adiciona uma nova chave e valor
idades["Cris"] = 55  # altera o valor de uma chave existente
print(idades)

# dicionario de mensagem:
# role = user / assistant / system
# content = texto da mensagem
mensagem1 = {"role": "assistant", "content": "Vamos criar uma IA?"}
mensagem2 = {"role": "user", "content": "Bora!"}
mensagem3 = {"role": "assistant", "content": "Então vamos lá!"}

# varias mensagens:
lista_mensagens = [mensagem1, mensagem2, mensagem3]

nova_mensagem = {"role": "user", "content": "Qual o seu nome?"}
lista_mensagens.append(nova_mensagem)  # adiciona nova mensagem na lista

print(lista_mensagens)

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
   # pip install python-dotenv para instalar a biblioteca que carrega variaveis de ambiente do arquivo .env
