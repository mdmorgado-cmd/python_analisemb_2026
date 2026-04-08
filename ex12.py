#calculo de notas de um colegio:
nota1 = float(input("Primeira nota: "))
print (nota1)
nota2 = float(input("Segunda nota: "))
print (nota2)

nota3 = float(input("Terceira nota: "))

media = (nota1 + nota2+ nota3) / 3
print ("############################# ")
if media >= 6:
    print ("APROVADO")
else:
    print ("REPROVADO")

print (f"Media entre as notas:  {media}")
print ("############################# ")
print (f"Primeira Nota: {nota1} ")

print (f"Segunda Nota: {nota2} ")

print (f"Terceira Nota:  {nota3}")

print ("############################# ")

