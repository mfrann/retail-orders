#=== IMPORTS ===#
from extract import extract_csv
from transform import (
    change_datatype,
    create_dim_products,
    create_dim_customers, 
    create_dim_locations,
    create_dim_ship
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


    # - Crear dimension de lugar
    print('\nDIMENSION DE LUGAR\n')
    dim_locations = create_dim_locations(df_retail)
    # Validar resultados
    print(f'\n Total lugares únicos: {len(dim_locations)}')
    print(f"\n Primeras 5 filas:\n{dim_locations.head()}")
    print(f"\n Últimas 5 filas:\n{dim_locations.tail()}") 
    print(f'\n [location_key] únicos: {dim_locations['location_key'].is_unique}')
    print(f'\n Regiones únicos: {dim_locations['Region'].value_counts()}')
    print(f'\n Países únicos:\n{dim_locations['Country'].unique()}')
    print(f'\n Combinaciones City+State+Postal únicas: {dim_locations[['City', 'State', 'Postal Code']].duplicated().sum()}')

    
    # - Crear dimension de envio
    print('\nDIMENSION DE ENVIO\n')
    dim_ship = create_dim_ship(df_retail)
    # Validar resultados
    print(f"\n Total envios únicos: {len(dim_ship)}")
    print(f" Columnas: {dim_ship.columns.tolist()}")
    print(f"\n Primeras 5 filas:\n{dim_ship.head()}")
    print(f"\n Últimas 5 filas:\n{dim_ship.tail()}")
    print(f"\n Hay nulos?: {dim_ship.isnull().sum().sum()}")






    return df_retail




run_app()