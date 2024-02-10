#old style %

nome = "Jungkook"
idade = 25
profissao = "cantor"
idioma = "coreano"

print("Ola, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e meu idioma eh %s." % (nome, idade, profissao, idioma))
#Ola, me chamo Jungkook. Eu tenho 25 anos de idade, trabalho como cantor e meu idioma eh coreano.

#evolução do old style - FORMAT
nome = "Jungkook"
idade = 25
profissao = "cantor"
idioma = "coreano"
pessoa = {"nome": "Jungkook", "idade": 20}
print("Ola, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e meu idioma eh {}.".format(nome, idade, profissao, idioma))
print("Ola, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e meu idioma eh {0}.".format(idioma, profissao, idade, nome))
print("Ola, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e meu idioma eh {idioma}.".format(nome = nome, idade = idade, profissao = profissao, idioma = idioma))
print("Ola, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e meu idioma eh {idioma}.".format(**pessoa))

#F-string
nome = "Jungkook"
idade = 25
profissao = "cantor"
idioma = "coreano"

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e falo {idioma}.")

#formatar strings com f-string
PI = 3.14159
print(f"Valor de PI: {PI:.2f}")
#valor de PI: 3.14

print(f"Valor de PI: {PI:10.2f}") #10 espaços
#valor de PI:           3.14
