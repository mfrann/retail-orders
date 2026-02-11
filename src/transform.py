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

# TODO: Crear dimension de fecha -- POR TERMINAR
def create_dim_dates(df):
    try:
        # ? Objetivo: Crear tabla con fechas unicas del dataset

        log.info("Creando dimensión de fechas...")
        # -- Extraer columnas
        order_date = df['Order Date']
        ship_date = df['Ship Date']

        # -- Concatenar las columnas
        df_dates = pd.concat([order_date, ship_date], ignore_index=True)

        # -- Fechas unicas 
        unique_dates = df_dates.unique()

        # -- Ordenar 
        unique_dates = pd.Series(unique_dates).sort_values()

        # -- Crear DataFrame
        df_dates = pd.DataFrame(unique_dates, columns=['date'])

        # -- Resetear index
        df_dates = df_dates.reset_index(drop=True)

        # -- Extraer componentes de fecha

        df_dates['date_key'] = range(len(df_dates))
        df_dates['year'] = df_dates['date'].dt.year
        df_dates['quarter'] = df_dates['date'].dt.quarter
        df_dates['month'] = df_dates['date'].dt.month
        df_dates['month_name'] = df_dates['date'].dt.month_name()
        df_dates['day'] = df_dates['date'].dt.day
        df_dates['day_of_week'] = df_dates['date'].dt.dayofweek
        df_dates['day_name'] = df_dates['date'].dt.day_name()
        df_dates['week_of_year'] = df_dates['date'].dt.isocalendar().week

        # -- Reordenar columnas
        df_dates = df_dates[['date_key', 'date', 'year', 'quarter', 'month', 'month_name', 'day', 'day_of_week', 'day_name', 'week_of_year']]

        log.info(f"Dimensión de fechas creada: {len(df_dates)} fechas únicas")
        return df_dates
    except KeyError as e:
        log.error(f'Columna no encontrada: {e}')
        return None
    except Exception as e:
        log.error(f'Error en create_dim_dates: {e}')
        return None


# TODO: Crear dimension de fact_sales
