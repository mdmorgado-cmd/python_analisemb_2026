########### função para retornar par ou impar

def numero  (a):
    if a % 2 == 0:
     return "par"
    else: 
     return"Ímpar"


v = int(input("Digite o numero: "))
y=numero(v)
print(y)