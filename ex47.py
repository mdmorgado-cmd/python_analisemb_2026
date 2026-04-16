def somar(a, b):
    return a + b
def subt(a, b):
    return a - b
def mult(a, b):
    return a * b
def div(a, b):
    if b != 0:
        return a/b
    else:
        print("valor invalido")

escolha = ""
while escolha != "0":
    escolha = input("digite uma opção 1-somar, 2-subtração, 3-multiplicação, 4-dividir ")
    num1 = int(input(" digite o primeiro numero "))
    num2 = int(input(" digite o segundo numero "))
    if escolha == "1":
        x= somar(num1, num2)
    elif escolha =="2":
        x= subt(num1, num2)
    elif escolha == "3":
        x= mult(num1, num2)
    else:
         x= div(num1, num2)

    print(f"O resultado da operação é {x}")

else:
    print("Operação Terminada") 

