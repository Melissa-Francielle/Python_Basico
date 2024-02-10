curso = "Cuso de python"
frutas = ["Laranja", "Uva", "Limão"]
saques = [1500, 100]

"Python" in curso 
#true

"maçã" not in frutas
#true

200 in saques
#false

print("\nExemplos")
Frutas = ["Limão", "uva"]
print("Laranja" in Frutas)
#false
Frutas = ["Limão", "uva", "Laranja"]
print("Laranja" in Frutas)
#true
#É case sensitive, significa que analisa até mesmo se é maiuscula ou miniscula 
print("Limão" not in Frutas)
#true
print("Laranja" not in Frutas)
#true
print("Limão" not in Frutas)
#true
curso = "curso de python"
print("Python" in curso)
#false
curso = "curso de Python"
print("Python" in curso)
#true
