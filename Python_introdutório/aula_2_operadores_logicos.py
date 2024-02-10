saldo =1000
saque  = 200
limite = 100
saldo >= saque
#true 
saque <= limite 
#false

#operador E
saldo = 1000
saque = 200
limite = 100
saldo >= saque and saque <= limite
#false

#operador ou 
saldo = 1000
saque = 200
limite =  100
saldo >= saque or saque <= limite
#true 

#operador de negação  NOT
contatos_emergencia = [] #lista vazia em pyhton tem seu valor booleano falso 
not 1000 > 1500
#true
not contatos_emergencia
#true
not "saque 1500;"
#false
not"" #vazia também é considerada falsa
#true

#parênteses
saldo = 1000
saque = 250
limite = 200
conta_especial = True 
saldo >= saque and saque <= limite or conta_especial and saldo >= saque 
#true
(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
#true 

print("Exemplo")
#AND - Para ser true tudo tem que ser true 
# OR - Para ser true apenas um deve ser true 

print(True and True)
print(True and False)
print(False and False)
print(True or False)
print(True or False)
print(False or False)


saldo = 1000
saque = 250
limite = 200
conta_especial = True 

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque 
#true
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
#true 
print(exp_2)

conta_normal_com_Saldo_fuciente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque 

exp_3 = conta_normal_com_Saldo_fuciente or conta_especial_com_saldo_suficiente
print(exp_3)
