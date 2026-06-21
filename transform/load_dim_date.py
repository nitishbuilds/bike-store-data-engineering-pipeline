import pandas as pd
from sqlalchemy import text
from load.db_connection import get_engine

engine = get_engine()

# Purana dim_date data hatao
with engine.begin() as conn:
    conn.execute(
        text("TRUNCATE TABLE warehouse.dim_date CASCADE")
    )

query = """
SELECT DISTINCT order_date
FROM staging.stg_orders
"""

df = pd.read_sql(query, engine)

df["order_date"] = pd.to_datetime(df["order_date"])

dim_date = pd.DataFrame({
    "date_key": df["order_date"].dt.strftime("%Y%m%d").astype(int),
    "full_date": df["order_date"],
    "year": df["order_date"].dt.year,
    "quarter": df["order_date"].dt.quarter,
    "month": df["order_date"].dt.month,
    "month_name": df["order_date"].dt.month_name(),
    "day": df["order_date"].dt.day,
    "day_name": df["order_date"].dt.day_name()
})

dim_date.to_sql(
    "dim_date",
    engine,
    schema="warehouse",
    if_exists="append",
    index=False
)

print("dim_date loaded")
