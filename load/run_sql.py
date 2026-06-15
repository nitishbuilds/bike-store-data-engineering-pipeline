from pathlib import Path
from sqlalchemy import text

from load.db_connection import get_engine


def execute_sql_file(file_path):
    engine = get_engine()

    with open(file_path, "r") as file:
        sql = file.read()

    with engine.begin() as conn:
        conn.execute(text(sql))

    print(f"Executed: {file_path}")


if __name__ == "__main__":
    execute_sql_file("sql/create_staging_schema.sql")
    execute_sql_file("sql/create_staging_tables.sql")

    execute_sql_file("sql/create_warehouse_schema.sql")
    execute_sql_file("sql/create_warehouse_tables.sql")
    execute_sql_file("sql/create_dim_date.sql")
