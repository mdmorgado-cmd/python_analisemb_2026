v=float(input("Digite o valor do item: "))
if v < 100:
    p=v*0.05
    d=v-p
elif v<499:
    p=v*0.15
    d=v-p
else:
    p=v*0.20
    d=v-p
print(f"O valor de {v} com desconto de {p} ficará em {d}: ")