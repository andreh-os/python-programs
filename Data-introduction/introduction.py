import pandas as pd

pd.Series(data=5) # Cria uma Series com o valor a

lista_nomes = 'Howard Ian Peter'.split()

pd.Series(lista_nomes) # Cria uma Series com uma lista de nomes

dados = {
    'nome1': 'Howard',
    'nome2': 'Ian',
    'nome3': 'Peter',
    'nome4': 'Jonah',
    'nome5': 'Kellie,'
}

pd.Series(dados) # Cria uma Series com um dicionário

cpfs = '111.111.111-11 222.222.222-22 333.333.333-33'.split()

pd.Series(lista_nomes, index=cpfs)

series_dados = pd.Series(lista_nomes,index=cpfs)

series_dados.loc['111.111.111-11']

print(series_dados.loc)