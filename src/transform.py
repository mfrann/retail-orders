#=== LIBRERIAS ===#
import pandas as pd
import logging as log
#=================#

'''
#TODOS:
# TODO: Cambiar tipo de datos   --COMPLETADO
# TODO: Crear dimension de productos    --COMPLETANDO...
'''


# TODO: Cambiar tipo de datos
def change_datatype(df):
    # -- Para cambiar a datatime
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])

    print(f'✓ Order Date cambiada a datatime')
    print(f'✓ Ship Date cambiada a datatime')

    print(f'\nTabla actualizada:\n {df.dtypes}\n')
    return df

    #Se ha cambiado los tipos de datos de las columnas Order Date y Ship Date a datatime.

# TODO: Crear dimension de productos
def create_dim_products(df):
    try:
        #? -- Objetivo: Crear una tabla con los productos unicos del dataset.

        if df is None:
            raise ValueError('DataFrame es None')
        # -- Seleccionar las columnas
        df_products = df[['Product ID', 'Product Name', 'Category', 'Sub-Category']]

        # -- Eliminar filas duplicadas
        df_products = df_products.drop_duplicates()

        # -- Resetar el indice 
        df_products = df_products.reset_index(drop=True)

        # -- Crear nueva columna product_key
        df_products['product_key'] = range(len(df_products)) # -> Crea la columna nueva y añade los indices. 

        # -- Reordenar columnas
        df_products = df_products[['product_key', 'Product ID', 'Product Name', 'Category', 'Sub-Category']]
    
    except KeyError as e:
        log.error(f'Columna no encontrada: {e}')
        return None
    except Exception as e:
        log.error(f'Error en create_dim_products')
        return None
    
    return df_products

# TODO: Crear dimension de clientes
def create_dim_customers(df):
    try:
        #? -- Objetivo: Crear una tabla con clientes unicos del dataset. 
        if df is None:
            raise ValueError('DataFrame es None')
        # -- Seleccionar las columnas
        df_customers = df[['Customer ID', 'Customer Name', 'Segment']]

        # -- Eliminar filas duplicadas 
        df_customers = df_customers.drop_duplicates(subset=['Customer ID']) # -> No es necesario, pero se evita un error.

        # -- Resetear indice
        df_customers = df_customers.reset_index(drop=True)

        # -- Crear columna 'customer_key'
        df_customers['customer_key'] = range(len(df_customers))

        # -- Reordenar columnas
        df_customers = df_customers[['customer_key', 'Customer ID', 'Customer Name', 'Segment']]

    except KeyError as e:
        log.error(f'Columna no encontrada: {e}')
        return None
    except Exception as e:
        log.error(f'Error en create_dim_customers')
        return None
    
    return df_customers

# TODO: Crear dimension de lugar
def create_dim_locations(df):
    try:
        #? -- Objetivo: Crear una tabla con los lugares unicos del dataset.

        if df is None:
            raise ValueError('DataFrame es None')
        # -- Seleccionar las columnas 
        df_locations = df[['Country', 'Region', 'State', 'City', 'Postal Code']]

        # -- Eliminar filas duplicadas
        df_locations = df_locations.drop_duplicates()

        # -- Resetear indice
        df_locations = df_locations.reset_index(drop=True)

        # -- Crear columna 'customer_key'
        df_locations['location_key'] = range(len(df_locations))

        # -- Reordenar columnas
        df_locations = df_locations[['location_key', 'Country', 'Region', 'State', 'City', 'Postal Code']]
    
    except KeyError as e:
        log.error(f'Columna no encontrada: {e}')
        return None
    except Exception as e:
        log.error(f'Error en create_dim_locations')
        return None
    
    return df_locations

# TODO: Crear dimension de modo de envio
def create_dim_ship(df):
    try:
        #? -- Objetivo: Crear una tabla con los envios unicos del dataset.

        if df is None:
            raise ValueError('DataFrame es None')
        # -- Seleccionar las columnas
        df_ship = df[['Ship Mode']]

        # -- Eliminar filas duplicadas
        df_ship = df_ship.drop_duplicates()

        # -- Resetear indice
        df_ship = df_ship.reset_index(drop=True)

        # -- Crear columna  'ship_mode_key'
        df_ship['ship_mode_key'] = range(len(df_ship))

        # -- Reordenar columnas 
        df_ship = df_ship[['ship_mode_key', 'Ship Mode']]
    
    except KeyError as e:
        log.error(f'Columna no encontrada: {e}')
        return None
    except Exception as e:
        log.error(f'Error en create_dim_ship')
        return None
    
    return df_ship

# TODO: Crear dimension de fecha
def create_dim_dates(df):
    try:
        # ? Objetivo: Crear tabla con fechas unicas del dataset

        # -- Seleccionar columnas
        df_dates = df[['Order Date', 'Ship_Date']]

        # -- Eliminar filas duplicadas
        df_dates = df_dates.drop_duplicates()

    except KeyError as e:
        log.error(f'Columna no encontrada: {e}')
    except Exception as e:
        log.error(f'Error en create_dim_dates')
    
    return df_dates
# TODO: Crear dimension de fact_sales