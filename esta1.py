import pandas as pd
dados = {'Vendedor' : ['natuto', 'Goku', 'Seiya'],
         'produto' : ['geladeira', 'Fogao', 'ar condicionado'],
         'Valor Produto' : [3400, 750, 2650]}
df = pd.DataFrame (dados)
print (df)
