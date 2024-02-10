#positional only
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
#              /obrigatório passar   /  já pode passar   
#                por  posicao \             por posição\
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="gasolina") #valido 

criar_carro(modelo = "Palio", ano =1999, placa= "ABC*1234", marca="Fiat", motor="1.0", combustivel="gasolina") #invalido 

#keyword only 
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
#              /obrigatório passar   /  já pode passar  
#                por  chave \             por chave\
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo = "palio", ano= 1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="gasolina") #valido 

criar_carro("Palio", 1999, "ABC*1234", marca="Fiat", motor="1.0", combustivel="gasolina") #invalido 

#keyword and positional only 
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
#              /obrigatório passar   /  já pode passar   
#                por  posição \           e por chave\
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #valido 

criar_carro(modelo="Palio", ano =1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #invalido 

#também é possivel ser dessa forma 
#def criar_carro(modelo, ano, placa, /, marca, *, motor, combustivel):
#                                       ~~~~~
# onde Marca seria basicamente tanto posição quanto chave, ou seja, poderia ser passada
# tanto por chave quanto por posição 
# chave => marca = "fiat" || posição => "Fiat"

#objetos de primeira classe
def somar(a, b):
    return a+b

def exibir_resultado(a, b, funcao):
    resultado = funcao (a, b)
    print(f"O resultado da operaçao {a} + {b} = {resultado}")

exibir_resultado(10, 10, somar) #resultado da operação 10+10=20


#variaveis locais e globais 
salario = 2000

def salario_bonus (bonus):
    global salario
    salario += bonus
    return salario

novo = salario_bonus(500) #2500
print(novo)

def salario_bonus (bonus, lista):
    global salario
    salario += bonus
    return salario

lista = [1]
novo = salario_bonus(500, lista) #2500
print(novo)
print(lista)

def salario_bonus (bonus, lista):
    global salario
    lista.append(2)
    salario += bonus
    return salario

lista = [1]
novo = salario_bonus(500, lista) #2500
print(novo)
print(lista)
#Mesmo do metodo ter sido encerrado a lista ainda continuou
# a lista é um objeto imutavel, então tudo que é feito na lista, vai ser refletido no objeto do lado de fora
# passado por referencia 
#  então se não quer que isso ocorra

#passe por copia 
def salario_bonus (bonus, lista):
    global salario
    lista_nova = lista.copy()
    lista_nova.append(2)
    print(f"Lista nova: {lista_nova}") #[1, 2]

    salario += bonus
    return salario

lista = [1]
novo = salario_bonus(500, lista) #2500
print(novo)
print(lista) #[1]