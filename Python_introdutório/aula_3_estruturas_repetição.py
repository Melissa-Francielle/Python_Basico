#Receba um numero do teclado e exiba os 2 numeros seguintes 
a = int (input ("Informe um numero inteiro: "))

a += 1
print(a)

a += 1
print(a)

#exemplo com repetição 

a = int(input("Informe um numero inteiro: "))

#repita 2 vezes:
#a += 1
#print (a)

texto = input("Informe um texto")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print() #adiciona uma quebra de linha 

print("for / else")
texto = input("Informe um texto")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print() #adiciona uma quebra de linha 
    print("executa no final do laço")
   

print("função range")
#range(stop) -> range object
#range(Start, stop[, step]) -> range object 
list (range(4))
#[0, 1, 2, 3]

print("Range com o for")
for numero in range(0, 11):
    print(numero, end=" ")

#0 1 2 3 4 5 6 7 8 9 10

#exibindo a tabuada do 5 
for numero in range (0, 51, 5):
    print(numero, end= " ")
#0 5 10 15 20 25 30 35 40 45 50

print("While")
opcao = -1

while opcao != 0:
    opcao = int(input("[1] sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao ==2:
        print("exibindo o extrato...")

print("While / else")

while opcao != 0:
    opcao = int (input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por usar nosso sistema bancario, até logo")

    opcao = -1

print("break...")
while True: #loop infinito 
    numero = int(input("Informe um numero"))

    if numero == 10:
        break
    print(numero)