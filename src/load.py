from importlib.resources import path
import sqlite3 
from pathlib import Path
import logging as log

BASE_DIR = Path(__file__).resolve().parent.parent
PROCESS_DIR = BASE_DIR / "data" / "processed"
DATA_DIR = BASE_DIR / "data" / "database"

def load_db(dimensions, fact_sales):

    try: 

        db_path = DATA_DIR / "superstore.db"

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # -- Cargar dimensiones
        dimensions['products'].to_sql('dim_products', conn, if_exists='replace', index=False)
        dimensions['customers'].to_sql('dim_customers', conn, if_exists='replace', index=False)
        dimensions['locations'].to_sql('dim_locations', conn, if_exists='replace', index=False)
        dimensions['dates'].to_sql('dim_dates', conn, if_exists='replace', index=False)
        dimensions['ship_modes'].to_sql('dim_ship', conn, if_exists='replace', index=False)

        # -- Cargar fact sales
        fact_sales.to_sql('fact_sales', conn, if_exists='replace', index=False)

        # -- Crear indices 
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_product_key ON fact_sales(product_key)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_customer_key ON fact_sales(customer_key)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_location_key ON fact_sales(location_key)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_order_date_key ON fact_sales(order_date_key)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_ship_date_key ON fact_sales(ship_date_key)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_ship_mode_key ON fact_sales(ship_mode_key)")
        conn.commit()

        print(f"✓ Base de datos actualizada: {db_path}")
        
    except Exception as e:
        log.error(f"Error al cargar datos en la base de datos: {e}")
        return None


def save_to_csv(df, filename):
    PROCESS_DIR.mkdir(exist_ok=True)

    path = PROCESS_DIR / filename
    df.to_csv(path, index=False)

    print(f"✓ Archivo guardado: {path}")