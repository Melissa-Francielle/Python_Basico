pessoa = {"nome": "Guilherme", "idade": 28}

pessoa = dict(nome = "Guilherme", idade=28)

pessoa["telefone"] = "3333-1234" #add uma nova chave a ele
#{"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

#acessando dados
dados = {"nome": "Guilherme", "idade": 28}

dados["nome"] #"Guilherme"
dados["idade"] #28
dados["telefone"] #3333-1234

dados["nome"] = "Maria"
dados["idade"] = 18
dados ["telefone"] = "9988-1787"

dados #{nome:"maria", "idade":18, "telefone":"9988-1781"}

#Dicionarios aninhados
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}, #para um dicionario esta se adicionando um novo dicionario 
    "gioavanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},   
}

contatos["gioavanna@gmail.com"]["telefone"] #"3443-2121"
#       (acessa o primeiro      (acessa o 
#           dicionario)         outro dicionario) 


#interar um dicionario 
for chave in contatos: #acessa so o email expressado, ou seja, o primeiro dicionario
    print(chave, contatos[chave]) #para acessar os dados do dicionario colocasse o contato[chave]
    #não é a melhor forma 

for chave, valor in contatos.items(): 
    print(chave, valor)

#   "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}, #para um dicionario esta se adicionando um novo dicionario 
#   "gioavanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
#   "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
#   "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"}, 