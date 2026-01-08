#=== IMPORTS ===#
from extract import extract_csv
from transform import (
    change_datatype
)
#===============#

def run_app():

    # -- EXTRAER EL DATAFRAME
    print("\nExtrayendo dataframe deel archivo superstore.csv...\n")
    
    df_retail = extract_csv()

    # -- TRANSFORM

    # - Cambiar tipo de dato
    print('\nCambiando tipo de dato al correcto.\n')
    change_datatype(df_retail)
    
    
    return df_retail

run_app()