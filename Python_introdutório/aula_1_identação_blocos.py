#bloco em python 
# caractere de método " : "
def scar(self, valor: float) -> None: #incio do bloco do metodo 
    if self.saldo >= valor:
    
        self.saldo -= valor

    #fim do bloco do if 
#fim do bloco do método

#exemplo sem os blocos de indentação
# Não funciona 
#def scar(self, valor: float) -> None:#inicio do bloco do metodo 
#if self.saldo >= valor: #inicio do bloco do if 
#self.saldo -= valor
#fim do bloco do if 
#fim do bloco do método 

print("\nExemplo")

def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Valor sacado")
        print("retire o seu dinheiro da boca do caixa")

    print("Obrigado por ser nosso cliente, tenha um bom dia!")

def depositar(valor):
    saldo = 500
    saldo += valor


sacar (1000)


