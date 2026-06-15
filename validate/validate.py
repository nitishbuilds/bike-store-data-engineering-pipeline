from load.db_connection import get_engine
import pandas as pd


def validate_table(table_name):
    engine = get_engine()

    query = f"""
    SELECT *
    FROM staging.{table_name}
    """

    df = pd.read_sql(query, engine)

    print(f"\n===== {table_name} =====")

    print(f"Rows: {len(df)}")

    print(f"Duplicates: {df.duplicated().sum()}")

    print(f"\nNull Values:")
    print(df.isnull().sum())


if __name__ == "__main__":

    tables = [
        "stg_customers",
        "stg_orders",
        "stg_order_items",
        "stg_products"
    ]

    for table in tables:
        validate_table(table)
