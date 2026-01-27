#=== IMPORTS ===#
from extract import extract_csv
from transform import (
    change_datatype,
    create_dim_products,
    create_dim_customers
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

    # - Crear dimension de productos
    print('\nDIMENSION DE PRODUCTOS\n')
    dim_products = create_dim_products(df_retail)
    # Validar resultados
    print(f"\n Total productos únicos: {len(dim_products)}")
    print(f" Columnas: {dim_products.columns.tolist()}")
    print(f"\n Primeras 5 filas:\n{dim_products.head()}")
    print(f"\n Últimas 5 filas:\n{dim_products.tail()}")
    print(f"\n Hay nulos?: {dim_products.isnull().sum().sum()}")

    # - Crear dimension de clientes
    print('\nDIMENSION DE CLIENTES\n')
    dim_customers = create_dim_customers(df_retail)
    # Validar resultados
    print(f"\n Total clientes únicos: {len(dim_customers)}")
    print(f" Columnas: {dim_customers.columns.tolist()}")
    print(f"\n Primeras 5 filas:\n{dim_customers.head()}")
    print(f"\n Últimas 5 filas:\n{dim_customers.tail()}")
    print(f"\n Hay nulos?: {dim_customers.isnull().sum().sum()}")





    return df_retail




run_app()