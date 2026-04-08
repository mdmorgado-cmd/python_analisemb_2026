#calcule a idade da pessoa 

nome = (input("Mome: "))

ano_nac = float (input("Ano de Nascimento: "))

ano_atual = float (input("Ano atual: "))

v_idade = ano_atual - ano_nac

genero = (input("Genero: "))


if v_idade >= 18 and genero.lower() == "m" :
    print (f"Ola {nome} voce tem  {v_idade} e esta apto para o Serviço militar")
    print ("############################# ")
else:
    print (f"Ola {nome} nao esta apto para o Serviço militar")
    print ("############################# ")

