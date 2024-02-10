#exemplo 

frutas = ['laranja', 'maca', 'uva']

frutas = [] #lista vazia

letras = list ('python')

numeros = list (range(10)) #gera valores de 0 a 9

carro = ['Ferrari', 'F8', 4200000, 2020, 2900, 'São Paulo', True]

#acesso direto
frutas =['maçã', 'laranja', 'uva', 'pera']

frutas[0] #maçã

frutas[2] #uva

#Indices negativos
frutas = ['maçã', 'laranja', 'uva', 'pera']
frutas[-1] #pera
frutas[-3] #laranja

#Listas Aninhadas
matriz = [
    [1, 'a', 2],
    ['b', 3, 4],
    [6, 5, 'c']

] #3x3 
matriz [0] #[1, 'a', 2]
matriz [0][0] #1
matriz [0][-1] #2
matriz [-1][-1] #'c'

#Fatiamento

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

#Compreensão de listas
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
        #append gera uma lista 

#filtro versão 2
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]

#explicando essa parte

pares = [numero for numero in numeros if numero % 2 == 0]
          #^    (                   ) (               )
        #retorno        for                 filtro
#retorno - é que vai compor a lista que vai ser geradad
#retorno e o for são obrigatórios 

#Como o python le essa informação 
'Ele intera <for> atribuindo cada item para variavel numeros'
'antes de retornar o numero ele vai fazer o filtro do <if>'

#modificando valores versão 1
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2) #elevando todos numeros lista ao quadrado


#modificando valores versão 2
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]
