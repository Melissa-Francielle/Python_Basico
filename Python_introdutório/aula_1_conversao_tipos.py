preco = 10
print(preco)
#10

preco = float(preco)
print(preco)
#10.0

preco = 10/2
print(preco)
#0.5

preco = 10.30
print(preco)
#10.3

preco = int (preco)
print(preco)
#10

preco = 10
print(preco)
#10

print(preco / 2)
#5.0

print(preco // 2) #consegue preservar o numero inteiro 
#5

#numero para string 
preco = 10.50
idade = 28

print(str(preco)) #convertendo para str
#10.5

print(str(idade)) #convertendo para str
#28

texto = f'idade {idade} preco {preco}' #concatenação segunda forma de alterar o tipo
print(texto)
#idade 28 preco 10.5


#string para numero 
preco = "10.50"
idade = "28"

print(float(preco)) #converte uma string para float 
#10.5

print(int(idade)) #converte a string para um inteiro
#28

#Erro de conversão 

##preco = "python"
##print(float(preco))
print('\n')
print('____________________________________________________________')
print('Revisao')

print (int (1.0)) #1
print (int (1.9))#1
print(int("10"))#10
print(float("10.10")) #10.1
print(float(100)) #100.0
print(str(10.10)) #10.1
print(type(str(10.10))) #ver o tipo - <class 'str'>

valor = 10
valor_str = str(valor) #str
print(type(valor))#int
print(type(valor_str))#str

print(100 / 2) #float
print(100 // 2) #int



