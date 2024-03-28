import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

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
             'LocalLesao',
             'TipoLesao',
             'SubTipoLesao',
             'CodigoEspecifico',
             'DadosPatologicos']
    target = 'Resultado'

    df = pd.read_csv(input_file, names=names)

    # Plotando o gráfico de dispersão
    plt.figure(figsize=(8, 6))
    plt.scatter(df['Pulso'], df['Idade'])
    plt.title("Gráfico de Dispersão: Idade vs. ExameRetal")
    plt.xlabel("Idade")
    plt.ylabel("ExameRetal")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()