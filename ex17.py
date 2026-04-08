# opção invalida :


nome = (input("Mome: "))


genero = (input("Genero: "))

if genero.lower() == "m":
    print (f"Ola {nome} seu genero  é  MASCULINO")

elif genero.lower() == "f":
    print (f"Ola {nome} seu genero  é  FEMININO")

else:
    print (f"GENERO INVALIDO")