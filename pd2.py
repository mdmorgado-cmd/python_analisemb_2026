import pandas as pd 

dados = {
    'cargos': ["assistente", "analista", "gerente", "diretor"],
    'salarios': [1000, 2000, 3000, 4000]
}

dados_bi = pd.DataFrame(dados)
print(dados_bi.head(2))
##print(dados_bi.to_string())
######print(dados_bi.tail(2))
#######print(dados_bi[2:4])
#####print(dados_bi.shape) 
