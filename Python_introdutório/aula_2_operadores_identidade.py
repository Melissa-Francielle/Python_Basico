curso = "Curso do python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso 
#true 

curso is not nome_curso
#false

saldo is limite
#true

print("\nEx")

saldo = 1000
limite = 500

print(saldo is limite)
#false
print(saldo is not limite)
#true
#agora se houver troca nos valores
saldo = 1000
limite = 1000

print(saldo is limite)
#true
print(saldo is not limite)
#false

