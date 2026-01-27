#=== LIBRERIAS ===#
import pandas as pd
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
    # -- Seleccionar las columnas
    df_products = df[['Product ID', 'Product Name', 'Category', 'Sub-Category']]
    print('Columnas seleccionadas')

    # -- Eliminar filas duplicadas
    df_products = df_products.drop_duplicates()
    print('Filas duplicadas eliminadas')

    # -- Resetar el indice 
    df_products = df_products.reset_index(drop=True)
    print('Indice Reseteado')

    # -- Crear nueva columna product_key
    df_products['product_key'] = range(len(df_products)) # -> Crea la columna nueva y añade los indices. 
    print('Nueva columna creada')

    # -- Reordenar columnas
    df_products = df_products[['product_key', 'Product ID', 'Product Name', 'Category', 'Sub-Category']]
    
    return df_products

# TODO: Crear dimension de clientes
def create_dim_customers(df):

    #? -- Objetivo: Crear una tabla con clientes unicos del dataset. 

    # -- Seleccionar las columnas
    df_customers = df[['Customer ID', 'Customer Name', 'Segment']]
    print('Columnas seleccionadas')

    # -- Eliminar filas duplicadas 
    df_customers = df_customers.drop_duplicates(subset=['Customer ID']) # -> No es necesario, pero se evita un error.
    print('Filas duplicadas eliminadas')

    # -- Resetear indice
    df_customers = df_customers.reset_index(drop=True)
    print('Indice Reseteado')

    # -- Crear columna 'customer_key'
    df_customers['customer_key'] = range(len(df_customers))
    print('Nueva columna creada')

    # -- Reordenar columnas
    df_customers = df_customers[['customer_key', 'Customer ID', 'Customer Name', 'Segment']]

    return df_customers

# TODO: Crear dimension de lugar
def create_dim_locations(df):

    #? -- Objetivo: Crear una tabla con las ubicaciones unicas del dataset.

    # -- Seleccionar las columnas 
    df_locations = df[['Country', 'Region', 'State', 'City', 'Postal Code']]
    print('Columnas seleccionadas')

    # -- Eliminar filas duplicadas
    df_locations = df_locations.drop_duplicates()
    print('Filas duplicadas eliminadas')

    # -- Resetear indice
    df_locations = df_locations.reset_index(drop=True)
    print('Indice Reseteado')

    # -- Crear columna 'customer_key'
    df_locations['location_key'] = range(len(df_locations))
    print('Nueva columna creada')

    # -- Reordenar columnas
    df_locations = df_locations[['location_key', 'Country', 'Region', 'State', 'City', 'Postal Code']]

    return df_locations

# TODO: Crear dimension de modo de envio
# TODO: Crear dimension de fecha
# TODO: Crear dimension de fact_sales