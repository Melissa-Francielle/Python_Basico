nome = "Guilherme Arthur de Carvalho"

nome[0] #Primeiro caracter
#G

nome[:9] #se nao informar o start e colocar dois pontos e um numero
            # ele vai começar do 0 e contar até o stop que é 9 
#"Guilherme"

nome[10:] #Começa do 10 posicao da string e ate o final, pois não esta informando a parada e sim só o começo 
#Arthur
#  
nome[10:16] #substring, pega um pedaço da string 
#Arthur

nome[10:16:2] #aqui esta informando start, stop, step 
#"Atu"          #começa em 10 para em 10 e da dois passos

nome[:] #nao passa start dois pontos e stop e so deixa os dois pontos, significa que ele vai passar a string toda
#"Guilherme Arthur de Carvalho"

nome [:: -1] #espelhar uma string 
#ohlavraC ed ruhtrA emrelhiuG
