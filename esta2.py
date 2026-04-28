import pandas as pd
dados = 'BaseDPEvolucaoMensalCisp.csv'
df = pd.read_csv(dados, encoding='latin-1', sep=';')
df
