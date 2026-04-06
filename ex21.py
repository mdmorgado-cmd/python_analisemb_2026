sal = float(input("QUAL O SEU SALARIO: "))
irrf = (sal * 7.5)/100
desc_sal = sal - irrf
irrf2 = (sal * 27)/100 
desc_sal2 = sal - irrf2

print ("############################# ")
if sal <= 5000:
    print (f"Nao tem desc de IRRF {sal}")

elif  sal <= 8000:
    print (f" valor do IRRF {irrf} ######## valor sal liquido {desc_sal}")
    
else: 
    print (f" valor do IRRF {irrf2} ######## valor sal liquido {desc_sal2}")
