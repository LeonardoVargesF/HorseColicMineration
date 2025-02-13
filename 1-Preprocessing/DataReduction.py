import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
#import pyperclip as pyper


def main():
    # Faz a leitura do arquivo
    input_file = '0-Datasets/ClearDataHorseModa.data'
    names = ['Cirurgia',
             'Idade',
             'NumeroHospital',
             'TemperaturaRetal',
             'Pulso',
             'FrequenciaRespiratoria',
             'TemperaturaExtremidades',
             'PulsoPeriferico',
             'MembranasMucosas',
             'TempoRecargaCapilar',
             'Dor',
             'Peristaltismo',
             'DistensaoAbdominal',
             'SondaNasogastrica',
             'RefluxoNasogastrico',
             'PHRefluxoNasogastrico',
             'ExameRetal',
             'Abdome',
             'VolumeCelulasEmbaladas',
             'ProteinaTotal',
             'AparenciaAbdominocentese',
             'ProteinaTotalAbdominocentese',
             'Resultado',
             'LesaoCirurgica',
             'LocalLesao',
             'TipoLesao',
             'SubTipoLesao',
             'CodigoEspecifico',
             'DadosPatologicos']
    features = ['Cirurgia',
             'Idade',
             'NumeroHospital',
             'TemperaturaRetal',
             'Pulso',
             'FrequenciaRespiratoria',
             'TemperaturaExtremidades',
             'PulsoPeriferico',
             'MembranasMucosas',
             'TempoRecargaCapilar',
             'Dor',
             'Peristaltismo',
             'DistensaoAbdominal',
             'SondaNasogastrica',
             'RefluxoNasogastrico',
             'PHRefluxoNasogastrico',
             'ExameRetal',
             'Abdome',
             'VolumeCelulasEmbaladas',
             'ProteinaTotal',
             'AparenciaAbdominocentese',
             'ProteinaTotalAbdominocentese',
             'LesaoCirurgica',
             'TipoLesao',
             'CodigoEspecifico',
             'DadosPatologicos']
    target = 'Resultado'
    df = pd.read_csv(input_file,    # Nome do arquivo com dados
                     names = names) # Nome das colunas                      
    ShowInformationDataFrame(df,"Dataframe original")

    # Separating out the features
    x = df.loc[:, features].values

    # Separating out the target
    y = df.loc[:,[target]].values

    # Standardizing the features
    x = MinMaxScaler().fit_transform(x)
    normalizedDf = pd.DataFrame(data = x, columns = features)
    normalizedDf = pd.concat([normalizedDf, df[[target]]], axis = 1)
    ShowInformationDataFrame(normalizedDf,"Dataframe Normalized")

    # PCA projection
    pca = PCA()    
    principalComponents = pca.fit_transform(x)
    print("Explained variance per component:")
    print(pca.explained_variance_ratio_.tolist())
    print("Teste:")
    print(principalComponents.tolist())


    print("\n\n")

    principalDf = pd.DataFrame(data = principalComponents[:,0:3], 
                               columns = ['principal component 1', 
                                          'principal component 2',
                                          'principal component 3'
                                          ])
    finalDf = pd.concat([principalDf, df[[target]]], axis = 1)    
    ShowInformationDataFrame(finalDf,"Dataframe PCA")
    
    VisualizePcaProjection(finalDf, target)


def ShowInformationDataFrame(df, message=""):
    print(message+"\n")
    print(df.info())
    print(df.describe())
    print(df.head(10))
    print("\n")
    
           
def VisualizePcaProjection(finalDf, targetColumn):
    fig = plt.figure(figsize = (8,8))
    ax = fig.add_subplot(111,projection = '3d') 
    ax.set_xlabel('Principal Component 1', fontsize = 15)
    ax.set_ylabel('Principal Component 2', fontsize = 15)
    ax.set_zlabel('Principal Component 3', fontsize = 15)
    ax.set_title('2 component PCA', fontsize = 20)
    targets = [1, 2, 3]
    colors = ['r', 'g', 'b']
    for target, color in zip(targets,colors):
        indicesToKeep = finalDf[targetColumn] == target
        ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'],
                   finalDf.loc[indicesToKeep, 'principal component 2'],
                   finalDf.loc[indicesToKeep, 'principal component 3'],
                   c = color, s = 50)
    ax.legend(targets)
    ax.grid()
    plt.show()


if __name__ == "__main__":
    main()