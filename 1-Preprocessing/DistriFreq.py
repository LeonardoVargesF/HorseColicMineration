import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

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
             'JogarFora',
             'JogarFora1',
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
             'Resultado',
             'LesaoCirurgica',
             'LocalLesao',
             'TipoLesao',
             'SubTipoLesao',
             'CodigoEspecifico',
             'DadosPatologicos']


    df = pd.read_csv(input_file,    # Nome do arquivo com dados
                     names = names) # Nome das colunas
                 
    #ShowInformationDataFrame(df,"Dataframe original")

    QntClasse = 3

    SepClasses = pd.cut(df['Pulso'], bins=QntClasse)
    print(SepClasses)

    FreqAbs = SepClasses.value_counts().sort_index()

    FreqAbs.sort_values()
    print(FreqAbs)


    plt.bar(FreqAbs.index.astype(str), FreqAbs.values)
    plt.xlabel('Classes')
    plt.ylabel('Frequência Absoluta')
    
    plt.show()
    #Criando um dataframe para a idade
    #dfi  = pd.DataFrame(df['TemperaturaRetal'], columns=['TemperaturaRetal'])
    #ShowInformationDataFrame(dfi,"Dataframe Temperatura Retal")

    #bins = [35, 36.5, 37.5, ]

#def ShowInformationDataFrame(df, message=""):
        #print(message+"\n")
        #print(df.info())
        #print(df.describe())
        #print(df.head(10))
        #print("\n") 
    
if __name__ == "__main__":
    main()