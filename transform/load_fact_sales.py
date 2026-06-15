from load.db_connection import get_engine

engine = get_engine()


def load_fact_sales():

    query = """
    INSERT INTO warehouse.fact_sales
    (
        order_id,
        product_id,
        customer_id,
        store_id,
        staff_id,
        quantity,
        list_price,
        discount,
        order_date
    )

    SELECT
        oi.order_id,
        oi.product_id,
        o.customer_id,
        o.store_id,
        o.staff_id,
        oi.quantity,
        oi.list_price,
        oi.discount,
        o.order_date

    FROM staging.stg_order_items oi

    JOIN staging.stg_orders o
    ON oi.order_id = o.order_id;
    """

    with engine.begin() as conn:
        conn.exec_driver_sql(query)

    print("fact_sales loaded")


if __name__ == "__main__":
    load_fact_sales()
