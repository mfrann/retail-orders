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

# TODO: Crear dimension de productos
def create_dim_products(df):
    # -- Seleccionar las columnas
    df_productos = df[['Product ID', 'Product Name', 'Category', 'Subcategory']]
    print('Columnas seleccionadas')
    # -- Eliminar filas duplicadas
    df_productos = df_productos.drop_duplicates()
    print('Filas duplicadas eliminadas')
    # -- Crear nueva columna product_key
    df['product_key'] = range(len(df))
    print('Nueva columna creada')
    # -- Resetar el indice 
    df_productos = df_productos.reset_index(drop=True)
    print('Indice Reseteado')