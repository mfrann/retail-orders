#=== LIBRERIAS ===#
import pandas as pd
from pathlib import Path
#=================#

#=== IMPORTS ===#
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "raw"
#===============#

'''
# TODOS:   ---COMPLETADO
# TODO: Cargar el CSV y entender la estructura
# TODO: Identificar columnas, tipos de datos, valores nulos
# TODO: Detectar duplicados y anomalías
# TODO: Documentar hallazgos
'''

# TODO: Cargar el CSV y entender la estructura  

def extract_csv():
    
    try:
        
       print('\nCargando archivo superstore.csv...\n')

       # --- Crear dataframe del archivo 
       df_retail = pd.read_csv(DATA_DIR / 'superstore.csv')

       print('\n✓ Archivo cargado correctamente\n')

    except FileNotFoundError as e:
        print(f'\n✗ Error: {e}\n')
        return None

    #Retornamos informacion de la tabla de superstore.csv
    print(f'\nDimensiones del dataset: {df_retail.shape}\n') 
    print(f'\nColumnas:\n{df_retail.columns.tolist()}\n')
    print(f'\nEstadísticas descriptivas:\n{df_retail.describe()}\n')

    #Retornamos los 5 primeras filas, contamos si hay nulos, tipos de dato
    print(f'\nPrimeras 5 filas:\n{df_retail.head()}\n')
    print(f'\nNulos:\n{df_retail.isnull().sum()}\n')
    print(f'\nTipos:\n{df_retail.dtypes}\n')
    print(f'\nDuplicados:\n{df_retail.duplicated().sum()}\n')


    return df_retail

'''
    No hay datos nulos o duplicados en el archivo superstore.csv
    Identifique los tipos de datos y es necesario cambiar el tipo de dato.
'''

if __name__ == '__main__':

    df = extract_csv()
    if df is not None:
        print("\n✓ Extracción completada exitosamente\n")


