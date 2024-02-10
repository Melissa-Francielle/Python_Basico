frutas = ("laranja", "pera", "uva",)

letras = tuple("python")

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil",)

#todos são declarações de tuple

#acessando os valores da tupla 
frutas = ("maça", "laranja", "uva", "pera")
#muito igual ao acesso da lista
frutas [0] #maça
frutas[2] #uva 

#indices negativos
frutas = ("maça", "laranja", "uva", "pera")
#muito igual ao acesso da lista
frutas [-1] #pera
frutas[-3] #laranja 


tabela =(
    (1, 'a', 2), #tupla1
    ('b', 3, 4), #tupla 2
    (6, 5, 'c'), #tupla 3
#3x3
)

tabela[0] # (1, 'a', 2),
tabela[0][0] #1
tabela[0][-1] #2
tabela[-1][-1] #c


#fatiamento 
lista = ['p', 'y', 't', 'h', 'o', 'n']
lista [2:] #'t', 'h', 'o', 'n'
lista [:2] #'p', 'y',
lista [1:3] #'y', 't',
lista [0:3:2] #'p' 't'
lista [::] #'p', 'y', 't', 'h', 'o', 'n'
lista [::-1] #'n' 'o' 'h' 't' 'y' 'p'


#Iterar listas
carros = ['gol', 'celta', 'palio']

for carro in carros:
    print(carro)

#Função enumerate 
carros = ['gol', 'celta', 'palio']

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
#indice seria o contador que inicia em 0

#métodos
#método [].count 

cores = ["vermelho", 'azul', 'verde', 'azul']

cores.count ("vermelho") #1
cores.count("azul") #2
cores.count("verde") #1

#método [].index

linguagens = ["python", 'js', 'c', 'java', 'csharp']

linguagens.index ("java") #3
linguagens.index("python") #0

#método len 
linguagens = ["python", 'js', 'c', 'java', 'csharp']

len(linguagens) #5