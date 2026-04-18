import pandas as pd 

dados = {
    'cargos': ["assistente", "analista", "gerente", "diretor"],
    'salarios': [1000, 2000, 3000, 4000]
}

dados_bi = pd.DataFrame(dados)

dados_bi.to_csv('meus_dados_cvs', index=False, sep=';', encoding='utf8')
###print(dados_bi.head(2))
print("############################")
print(dados_bi.to_string())
######print(dados_bi.tail(2))
#######print(dados_bi[2:4])
#####print(dados_bi.shape) 

print("############################")
print("arquivo criado com sucesso")