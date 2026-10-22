import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# OBTENDO OS DADOS

try:
    ENDERECO_DE_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    # criando data frame
    df_crimes = pd.read_csv(ENDERECO_DE_DADOS, sep=';', encoding = 'iso-8859-1')
    
    # delimitar dados
    df_cvli = df_crimes[['aisp', 'cvli']]
   
    # Preparar e ordenar os dados

    # totalizar crimes por batalhão

    df_cvli = df_cvli.groupby('aisp', as_index=False)['cvli'].sum()

    
    # Colocar em ordem decrescente

    df_cvli = df_cvli.sort_values(by='cvli', ascending=False)

    # print(df_cvli.head(30))
    # print(df_cvli.tail(30))

except Exception as e:
    print(f'Erro ao obter dados {e}')


# CRIANDO O ARRAY
    
try:
    array_cvli = np.array(df_cvli['cvli'])





except Exception as e:
    print(f'Erro ao criar um array {e}')