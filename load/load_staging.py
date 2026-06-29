from sqlalchemy import text

from load.db_connection import get_engine
from storage.s3_storage import load_csv

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
    # Read directly from AWS S3
    df = load_csv(file_name)

    engine = get_engine()

    # Clear existing data
    with engine.begin() as conn:
        conn.execute(
            text(f"TRUNCATE TABLE staging.{table_name} CASCADE")
        )

    # Load fresh data
    df.to_sql(
        name=table_name,
        con=engine,
        schema="staging",
        if_exists="append",
        index=False
    )

    print(f"Loaded {file_name} from S3 -> staging.{table_name}")


if __name__ == "__main__":
    for file_name, table_name in TABLE_MAPPING.items():
        load_table(file_name, table_name)
