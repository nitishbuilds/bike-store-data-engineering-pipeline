import pandas as pd
from pathlib import Path

RAW_DATA_PATH = Path("data/raw")


def load_csv(filename):
    file_path = RAW_DATA_PATH / filename
    return pd.read_csv(file_path)


def load_all_tables():
    tables = {}

    csv_files = [
        "brands.csv",
        "categories.csv",
        "customers.csv",
        "order_items.csv",
        "orders.csv",
        "products.csv",
        "staffs.csv",
        "stocks.csv",
        "stores.csv"
    ]

    for file in csv_files:
        table_name = file.replace(".csv", "")
        tables[table_name] = load_csv(file)

    return tables


if __name__ == "__main__":
    tables = load_all_tables()

    for name, df in tables.items():
        print("\n" + "=" * 50)
        print(f"TABLE: {name}")
        print("=" * 50)

        print(f"Rows: {df.shape[0]}")
        print(f"Columns: {df.shape[1]}")

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nFirst 3 Rows:")
        print(df.head(3))
