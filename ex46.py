###########função que retorna o maior numero      
def maior (a, b):
    if a > b:
        return (f"Maior numero é o Primeiro {a}")
    else:
        return (f"Maior numero é o Segundo {b}")
#verificação do maior numero :
numero  = float(input("Primeira numero: "))

numero2 = float(input("Segunda numero: "))

resultado = maior(numero, numero2)

print(resultado)