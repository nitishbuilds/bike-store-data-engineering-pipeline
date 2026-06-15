import pandas as pd
from pathlib import Path

from load.db_connection import get_engine

RAW_DATA_PATH = Path("data/raw")

TABLE_MAPPING = {
    "brands.csv": "stg_brands",
    "categories.csv": "stg_categories",
    "customers.csv": "stg_customers",
    "order_items.csv": "stg_order_items",
    "orders.csv": "stg_orders",
    "products.csv": "stg_products",
    "staffs.csv": "stg_staffs",
    "stocks.csv": "stg_stocks",
    "stores.csv": "stg_stores"
}


def load_table(file_name, table_name):
    df = pd.read_csv(RAW_DATA_PATH / file_name)

    engine = get_engine()

    df.to_sql(
        name=table_name,
        con=engine,
        schema="staging",
        if_exists="append",
        index=False
    )

    print(f"Loaded {file_name} -> staging.{table_name}")


if __name__ == "__main__":
    for file_name, table_name in TABLE_MAPPING.items():
        load_table(file_name, table_name)
