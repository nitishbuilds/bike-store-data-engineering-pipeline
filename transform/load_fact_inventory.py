from load.db_connection import get_engine

engine = get_engine()

query = """
INSERT INTO warehouse.fact_inventory
(
    store_id,
    product_id,
    quantity
)

SELECT
    store_id,
    product_id,
    quantity

FROM staging.stg_stocks;
"""

with engine.begin() as conn:
    conn.exec_driver_sql(query)

print("fact_inventory loaded")
