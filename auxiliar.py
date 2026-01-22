
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