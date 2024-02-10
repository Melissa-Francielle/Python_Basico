#{}.clear
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}, #para um dicionario esta se adicionando um novo dicionario 
    "gioavanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},   
}

contatos.clear()
contatos #{}

#{}.copy 

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}, #para um dicionario esta se adicionando um novo dicionario 

}

copia = contatos.copy()
copia ["guillherme@gmail.com"] #{"nome": "Guillherme", "telefone": "3333-2221"}

contatos["guillherme@gmail.com"] #{"nome": "Guillherme", "telefone": "3333-2221"}

copia ["guillherme@gmail.com"] #{'nome': 'Gui'}

#{}.fromkeys 
dict.fromkeys(['nome', 'telefone']) #{'nome': none,'telefone': none}

dict.fromkeys(["nome", "telefone"], 'vazio') #{'nome': 'vazio', 'telefone': 'vazio'}
#pode ser usado para dicionarios existentes e não existentes
# se for existentes é só trocar dict pelo nome do seu dicionario 

#{}.get
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}, #para um dicionario esta se adicionando um novo dicionario 

}
contatos['chave'] #KeyError 
#se colocar o nome da chave e não existir no dicionario ele lança uma excessão fazendo com que o programa pare

contatos.get('chave') #none
contatos.get('chave', {}) #{}
contatos.get('guilherme@gmail.com', {}) #{'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221}}

#items 
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}, #para um dicionario esta se adicionando um novo dicionario 

}

contatos.items() #dict_items([('guilherme@gmail.com': {"nome": "Guilherme", "telefone": "3333-2221"}, #para um dicionario esta se adicionando um novo dicionario})])

#keys
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}, #para um dicionario esta se adicionando um novo dicionario 

}
contatos.keys() #dict_keys(['guilherme@gmail.com])

#pop 
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}, #para um dicionario esta se adicionando um novo dicionario 

}
contatos.pop("guilherme@gmail.com") #{'nome': 'Guilherme', 'telefone': '3333-2221'}
contatos.pop("guilherme@gmail.com", {}) #{}

#{}.popitem 
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}, #para um dicionario esta se adicionando um novo dicionario 

}
contatos.popitem() #('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221})
contatos.popitem() #keyError

#{}.setdefault
contato = {"nome": "Guilherme", "telefone": "3333-2221"}, #para um dicionario esta se adicionando um novo dicionario 

contato.setdefault("nome", "Giovanna") #Guillherme
contato #{'nome': 'Guilherme", "telefone", '3333-2221"}

contato.setdefault("idade", 28) #28
contato #{'nome': 'Guilherme', 'telefone': '3333-2221", 'idade': 28}

#{}.update
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}, #para um dicionario esta se adicionando um novo dicionario 

}
contatos.uptade({"guilherme@gmail.com":{"nome": "Gui"}})
contatos #{"guilherme@gmail.com":{"nome": "Gui"}}

contatos.uptade({"giovanna@gmail.com": {'nome': 'Giovanna', 'telefone': '3322-8181'}})
contatos # #{"guilherme@gmail.com":{"nome": "Gui"}, 'giovanna@gmail.com': {'nome': 'Giovanna', "telefone": '3322-8181"}}

#{}.values 
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}, #para um dicionario esta se adicionando um novo dicionario 
    "gioavanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},   
}

contatos.values() 
#dict_values([{'nome': 'Guilherme', 'telefone': '3333-2221'}, {'nome': 'Giovanna', 'telefone': '3443-2121'}, {'nome': 'Chappie'
# 'telefone': 3344-9871"},{'nome': 'Melaine', 'telefone': '3333-7766'}])

#in 
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}, #para um dicionario esta se adicionando um novo dicionario 
    "gioavanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},   
}

"guilherme@gmail.com" in contatos #true 
"megui@gmail.com" in contatos #false
"idade" in contatos["guilherme@gmail.com"] #false
"telefone" in contatos ["giovanna@gmail.com"] #true 

#del
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}, #para um dicionario esta se adicionando um novo dicionario 
    "gioavanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},   
}
del contatos ["guiherme@gmail.com"]['telefone']
del contatos ["chappie@gmail.com"]

contatos #"guilherme@gmail.com": {"nome": "Guilherme"}, "gioavanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
#   "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"}, "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},   