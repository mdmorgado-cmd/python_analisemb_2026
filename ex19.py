v=float(input("Digite um valor"))
if v < 100:
    p = v * 0.05
    d = v - p
elif v < 499:
    p = v * 0.15
    d = v - p
else:
    p = v * 0.2
    d = v - p
    print(f"o valor de {v} com desconto {p} ficará em {d}")

