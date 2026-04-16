nota = 0
while nota >= 0 and nota <= 10:
    try:
            nota = int(input("digite uma nota entre 0 a 10:  "))
    except ValueError:
        print ("Entrada Valida. Por favor digite um numero")
print(f"Nota Invalida registrada: {nota}")




