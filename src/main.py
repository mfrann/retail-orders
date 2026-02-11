#=== IMPORTS ===#
from extract import extract_csv
from transform import (
    change_datatype,
    create_dim_products,
    create_dim_customers, 
    create_dim_locations,
    create_dim_ship,
    create_dim_dates
)
#===============#

def run_app():

    # -- EXTRAER EL DATAFRAME
    print("\nExtrayendo dataframe del archivo superstore.csv...\n")
    
    df_retail = extract_csv()

    # -- TRANSFORM

    # - Cambiar tipo de dato
    print('\nCambiando tipo de dato al correcto.\n')
    df_retail = change_datatype(df_retail)

    # - Crear dimension de productos
    print('\nDIMENSION DE PRODUCTOS\n')
    dim_products = create_dim_products(df_retail)
    if dim_products is None:
        print("Pipeline detenido: dim_products falló")
        return None
    # Validar resultados
    print(f"\n Total productos únicos: {len(dim_products)}")
    print(f" Columnas: {dim_products.columns.tolist()}")
    print(f"\n Primeras 5 filas:\n{dim_products.head()}")
    print(f"\n Últimas 5 filas:\n{dim_products.tail()}")
    print(f"\n Hay nulos?: {dim_products.isnull().sum().sum()}")

    # - Crear dimension de clientes
    print('\nDIMENSION DE CLIENTES\n')
    dim_customers = create_dim_customers(df_retail)
    if dim_customers is None:
        print("Pipeline detenido: dim_customers falló")
        return None
    # Validar resultados
    print(f"\n Total clientes únicos: {len(dim_customers)}")
    print(f" Columnas: {dim_customers.columns.tolist()}")
    print(f"\n Primeras 5 filas:\n{dim_customers.head()}")
    print(f"\n Últimas 5 filas:\n{dim_customers.tail()}")
    print(f"\n Hay nulos?: {dim_customers.isnull().sum().sum()}")


    # - Crear dimension de lugar
    print('\nDIMENSION DE LUGAR\n')
    dim_locations = create_dim_locations(df_retail)
    if dim_locations is None:
        print("Pipeline detenido: dim_locations falló")
        return None
    # Validar resultados
    print(f'\n Total lugares únicos: {len(dim_locations)}')
    print(f"\n Primeras 5 filas:\n{dim_locations.head()}")
    print(f"\n Últimas 5 filas:\n{dim_locations.tail()}") 
    print(f'\n [location_key] únicos: {dim_locations["location_key"].is_unique}')
    print(f'\n Regiones únicos: {dim_locations["Region"].value_counts()}')
    print(f'\n Países únicos:\n{dim_locations["Country"].unique()}')
    print(f'\n Combinaciones City+State+Postal únicas: {dim_locations[["City", "State", "Postal Code"]].duplicated().sum()}')

    
    # - Crear dimension de envio
    print('\nDIMENSION DE ENVIO\n')
    dim_ship = create_dim_ship(df_retail)
    if dim_ship is None:
        print("Pipeline detenido: dim_ship falló")
        return None
    # Validar resultados
    print(f"Total modos: {len(dim_ship)}")  
    print(f"Nulos: {dim_ship.isnull().sum().sum()}")  
    print(f"Duplicados: {dim_ship.duplicated().sum()}")
    print(f"ship_mode_key únicos: {dim_ship['ship_mode_key'].is_unique}") 
    print(f"Rango: {dim_ship['ship_mode_key'].min()} a {dim_ship['ship_mode_key'].max()}")  
    print(f"Modos únicos: {sorted(dim_ship['Ship Mode'].unique())}")
    print(f"Columnas: {dim_ship.columns.tolist()}")
    print(f"Tipos:\n{dim_ship.dtypes}")
    print(f"\nTabla completa:\n{dim_ship}")


    # - Crear dimension de date
    print('\nDIMENSION DE FECHA\n')
    dim_date = create_dim_dates(df_retail)
    if dim_date is None:
        print("Pipeline detenido: dim_date falló")
        return None
    # Validar resultados
    print(f"Total fechas únicas: {len(dim_date)}")
    print(f"Nulos: {dim_date.isnull().sum().sum()}")
    print(f"Duplicados: {dim_date.duplicated().sum()}")
    print(f"date_key únicos: {dim_date['date_key'].is_unique}")
    print(f"Rango: {dim_date['date_key'].min()} a {dim_date['date_key'].max()}")
    print(f"Columnas: {dim_date.columns.tolist()}")


    
    
    

    return df_retail
run_app()