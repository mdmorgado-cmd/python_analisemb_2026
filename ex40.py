sen_cor = "1234"
tents = 0
max_tent = 3
while tents < max_tent:
    tentativa = input(f"digite a senha(tentativa {tents + 1}/{max_tent}): ")
    if tentativa == sen_cor:
        print ("acesso concedido! ben vindo")
        break 
    else: 
        print ("senha incorreta")
        tents += 1 #####pegar o que tem dentro e soma mais vezes === e igual a isso tents = tent + 1
else:
    print("Voce execeu o numero maximo de tentativas--- acesso bloqueado")