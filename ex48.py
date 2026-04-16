def somar(a, b):
    return a + b
def subt(a, b):
    return a - b
def mult(a, b):
    return a * b
def div(a, b):
    if b != 0: 
       return a / b
    else:
        print("valor invalido")

    
escolha = ""
while escolha != 0:
    print("\n--- MENU ---")
    print("1-Somar, 2-Subtração, 3-Multiplicação, 4-Dividir, 0-Sair")
    try:
        escolha = int(input("Digite uma opção: "))
        
        if escolha == 0:
            print("Saindo...")
            break
        elif escolha in [1, 2, 3, 4]:
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
            if escolha == 1:
                print("Resultado:", somar(num1, num2))
            elif escolha == 2:
                print("Resultado:", subt(num1, num2))
            elif escolha == 3:
                print("Resultado:", mult(num1, num2))
            elif escolha == 4:
                print("Resultado:", div(num1, num2))
        else:
            print("Opção inválida! Digite um número entre 0 e 4.")
    except ValueError:
        print("Erro: Digite apenas números inteiros.")