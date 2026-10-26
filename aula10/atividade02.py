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

    print(df_cvli.head(30))
    print(df_cvli.tail(30))

except Exception as e:
    print(f'Erro ao obter dados {e}')


# CRIANDO O ARRAY
    
try:
    array_cvli = np.array(df_cvli['cvli'])


except Exception as e:
    print(f'Erro ao criar um array {e}')

# CALCULANDO MEDIDAS (TENDÊNCIA CENTRAL, POSIÇÃO, DISPERSÃO, QUARTIS ETC)

try:
    # MÉDIA, MEDIANA E DISTÂNCIA

    media_cvli = np.mean(array_cvli)
    mediana_cvli = np.median(array_cvli)
    distancia_cvli = abs(
        (media_cvli - mediana_cvli) / mediana_cvli * 100
    )
    # print(30*'=')
    # print(media_cvli)
    # print(mediana_cvli)
    # print(distancia_cvli)

    # QUARTIS
    q1 = np.quantile(array_cvli, .25)
    q2 = np.quantile(array_cvli, .50)
    q3 = np.quantile(array_cvli, .75)

    # print(30*'=')
    # print(f'Q1 : {q1}')
    # print(f'Q2 : {q2}')
    # print(f'Q3 : {q3}')

    # IQR, lIMITES INFERIOR E SUPERIOR

    iqr = q3 - q1
    #print(f'IQR: {iqr}')
    limite_inferior = q1 - (1.5 * iqr)
    limite_superior = q3 + (1.5 * iqr)

    # print(f'\nLimite Inferior: {limite_inferior}')
    # print(f'Limite Superior: {limite_superior}')

    # AMPLITUDE TOTAL, MENOR E MAIOR VALOR
    minimo = np.min(array_cvli)
    maximo = np.max(array_cvli)
    amplitude_total = maximo - minimo

   # print(f'\nAmplitude Total: {amplitude_total}')
    #print(f'Menor valor: {minimo}')
    #print(f'Maior valor: {maximo}')

    # VARIÂNCIA
    variancia = np.var(array_cvli)
    #print(f'\nVariância: {variancia}')

    # DISTÂNCIA ENTRE VARIÂNCIA E MÉDIA
    dist_med_var = variancia / (media_cvli ** 2) * 100
    #print(f'Distância entre variância e média: {dist_med_var}%')

    # DESVIO PADRÃO
    desvio_padrao = np.std(array_cvli)
    #print(f'Desvio Padrão: {desvio_padrao}')

    # COEFICIENTE DE VARIAÇÃO
    coef_var = (desvio_padrao / media_cvli) * 100
    #print(f'Coeficiente de Variação: {coef_var}%')


except Exception as e:
    print(f'Erro ao calcular medidas {e}')


# MOSTRAR AS MEDIDAS   

try:
     print('\n Mostrando Medidas')
     print(30*'-')
     print(f'Mínimo: {minimo}')
     print(f'Limite Inferior: {limite_inferior}')
     print(f'Q1: {q1}')
     print(f'Q2: {q2}')
     print(f'Q3: {q3}')
     print(f'Limite Superior: {limite_superior}')
     print(f'Maximo: {maximo}')
    
     print(f'\nMédia: {media_cvli}')
     print(f'Mediana: {mediana_cvli}')
     print(f'Distância: {distancia_cvli:.2f}%')
     print(f'IQR: {iqr}')
     print(f'Amplitude: {amplitude_total}')
     print(f'Variância: {variancia:.2f}')
     print(f'Distância entre Variância e Média: {dist_med_var:.2f}%')
     print(f'Desvio Padrão: {desvio_padrao:.2f}')
     print(f'Coeficiente de Variação: {coef_var:.2f}%')

except Exception as e:
    print(f'Erro ao apresentar as medidas {e}')


    # ORDENANDO BATALHÕES POR CRIMES E APRESENTANDO OUTLIERS


try:
    # BATALHÕES COM MENOS CRIMES

    print(30*'=')
    





except Exception as e:
    print(f'Erro ao apresentar batalhões')