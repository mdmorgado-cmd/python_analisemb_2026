#calcule a idade da pessoa 

nome = (input("Mome: "))

ano_nac = float (input("Ano de Nascimento: "))

ano_atual = float (input("Ano atual: "))

v_idade = ano_atual - ano_nac

if v_idade >= 18:
    print (f"Ola {nome} voce tem  {v_idade} e é MAIOR  DE IDADE")
    print ("############################# ")
else:
    print (f"Ola {nome} voce tem  {v_idade} e é MENOR  DE IDADE")
    print ("############################# ")

