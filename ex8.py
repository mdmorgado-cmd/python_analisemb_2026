#calcular o valor da porcentagem em real 

valor = float (input("valor da compra: "))

por =  float (input("qtos porcentos: ")) /100

valor_desc = valor * por 

valor_final = valor - valor_desc
print (f"Valor do desconto: {valor_desc} ")

print (f"Valor final da compra com desc:  {valor_final}")
