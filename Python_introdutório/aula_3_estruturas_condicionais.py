import sys


print("IF")

saldo = 2000.0
saque = float(input("Informe o valor do saque"))

if saldo >= saque:
    print("Realizando saque")

if saldo < saque:
    print("Saldo insuficiente")


print("IF ELSE")

saldo = 2000.0
saque = float(input("Inform o valor do saque"))

if saldo >= saque:
    print("Realizando saque")

else:
    print("Saldo insuficiente")

print("If else elif")

opcao = int(input("Informe uma opcao [1] Sacar\n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantidade para o saque: "))

elif opcao == 2:
    print("Exibindo o extrato...")

else:
    sys.exit("Opcao inválida")
    
print("If aninhado")

conta_normal = True 
conta_universitaria = False

saldo = 2000
saque = 500
cheque_especial = 450
if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente")

print("If ternario")

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")
