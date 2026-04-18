import pandas as pd
df = pd.read_csv('ClassicDisco.csv')

#####print(df.head(10)) ####### imprime apenas as 10 linhas 
####print(df.to_string()) ##### imprime tdas as linhas 
######print(df.tail(10)) ######imprime as 10 ultimas linhas
############print(df[10:20]) ##########imprime sa linhas de 10 a 20 
print(df.shape) ######## conta a qtda de linhas e colunas 

