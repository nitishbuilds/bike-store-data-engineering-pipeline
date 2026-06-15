import pandas as pd
from load.db_connection import get_engine

engine = get_engine()


def run_query(query, message):
    with engine.begin() as conn:
        conn.exec_driver_sql(query)

    print(message)


def load_dim_customer():
    query = """
    INSERT INTO warehouse.dim_customer
    (customer_id, first_name, last_name, city, state)

    SELECT
        customer_id,
        first_name,
        last_name,
        city,
        state
    FROM staging.stg_customers

    ON CONFLICT (customer_id)
    DO NOTHING;
    """

    run_query(query, "dim_customer loaded")


def load_dim_product():
    query = """
    INSERT INTO warehouse.dim_product
    (
        product_id,
        product_name,
        brand_id,
        category_id,
        model_year,
        list_price
    )

    SELECT
        product_id,
        product_name,
        brand_id,
        category_id,
        model_year,
        list_price

    FROM staging.stg_products

    ON CONFLICT (product_id)
    DO NOTHING;
    """

    run_query(query, "dim_product loaded")


def load_dim_store():
    query = """
    INSERT INTO warehouse.dim_store
    (
        store_id,
        store_name,
        city,
        state
    )

    SELECT
        store_id,
        store_name,
        city,
        state

    FROM staging.stg_stores

    ON CONFLICT (store_id)
    DO NOTHING;
    """

    run_query(query, "dim_store loaded")


def load_dim_staff():
    query = """
    INSERT INTO warehouse.dim_staff
    (
        staff_id,
        first_name,
        last_name
    )

    SELECT
        staff_id,
        first_name,
        last_name

    FROM staging.stg_staffs

    ON CONFLICT (staff_id)
    DO NOTHING;
    """

    run_query(query, "dim_staff loaded")


if __name__ == "__main__":
    load_dim_customer()
    load_dim_product()
    load_dim_store()
    load_dim_staff()
