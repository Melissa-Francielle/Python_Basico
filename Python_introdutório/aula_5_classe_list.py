#Método [].append

lista = []

lista.append(1)
lista.append("python")
lista.append([40, 30, 20])

print(lista) #[1, "python", [40, 30, 20]]

#Mét. [].Clear

lista = [1, "python", [40, 30, 20]]
print (lista) #[1, "python", [40, 30, 20]]

lista.clear()

print(lista) #[]

#comando [].copy

lista = [1, "python", [40, 30, 20]]

lista.copy()

print(lista) #[1, "python", [40, 30, 20]]

#método [].count 

cores = ["vermelho", 'azul', 'verde', 'azul']

cores.count ("vermelho") #1
cores.count("azul") #2
cores.count("verde") #1

#método [].extend

linguagens = ["python", 'js', 'c']

print(linguagens) #['python', 'js', 'c']

linguagens.extend(['java', 'csharp'])

print(linguagens) #["python", 'js', 'c', 'java', 'csharp']


#método [].index

linguagens = ["python", 'js', 'c', 'java', 'csharp']

linguagens.index ("java") #3
linguagens.index("python") #0

#método [].pop

linguagens = ["python", 'js', 'c', 'java', 'csharp']

linguagens.pop() #csharp
linguagens.pop() #java
linguagens.pop() #c
linguagens.pop(0) #python 
#chamar o pop ele sempre vai tirar o ultimo elemento da lista 


#método [].remove
linguagens = ["python", 'js', 'c', 'java', 'csharp']

linguagens.remove('c')

print(linguagens) #["python", 'js', 'java', 'csharp']

#método [].reverse
linguagens = ["python", 'js', 'c', 'java', 'csharp']

linguagens.reverse()

print(linguagens) # ['csharp, 'java', 'c', 'js', 'python]

#método [].sort
linguagens = ["python", 'js', 'c', 'java', 'csharp']
linguagens.sort() #['c', 'csharp', 'java', 'js', 'python']

linguanges = ["python", 'js', 'c', 'java', 'csharp']
linguagens.sort(reverse = True) #['python, 'js', 'java', 'csharp', 'c']

linguagens = ["python", 'js', 'c', 'java', 'csharp']
linguagens.sort (key = lambda x: len(x)) #['c', 'js', 'java', 'python', 'csharp']

linguagens = ["python", 'js', 'c', 'java', 'csharp']
linguagens.sort(key = lambda x: len(x), reverse = True) #['python', 'csharp', 'java', 'js', 'c']

#reverse 
#ordena, mas também pode fazer o espelhamento dessa lista 

#key 
#ordena por tamanho da palavra
#key = lambda x: len(x)) ordem crescente 
# lambda - função anonima / x - argumento que passa a ser aquele valor  
# len - verifica o tamanho das strings

#key = lambda x: len(x), reverse = True - ficou descrecente


#método len 
linguagens = ["python", 'js', 'c', 'java', 'csharp']

len(linguagens) #5

#sorted

linguagens = ["python", 'js', 'c', 'java', 'csharp']

sorted(linguagens, key=lambda x: len(x)) # ['c', 'js', 'java', 'python', 'csharp']

sorted(linguagens, key = lambda x: len(x), revese = True) #['python', 'csharp', 'java', 'js', 'c']

