CREATE TABLE IF NOT EXISTS warehouse.dim_customer (
    customer_key SERIAL PRIMARY KEY,
    customer_id INT UNIQUE,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS warehouse.dim_product (
    product_key SERIAL PRIMARY KEY,
    product_id INT UNIQUE,
    product_name VARCHAR(255),
    brand_id INT,
    category_id INT,
    model_year INT,
    list_price NUMERIC(10,2)
);

CREATE TABLE IF NOT EXISTS warehouse.dim_store (
    store_key SERIAL PRIMARY KEY,
    store_id INT UNIQUE,
    store_name VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS warehouse.dim_staff (
    staff_key SERIAL PRIMARY KEY,
    staff_id INT UNIQUE,
    first_name VARCHAR(100),
    last_name VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS warehouse.fact_sales (
    sales_key SERIAL PRIMARY KEY,

    order_id INT,
    product_id INT,
    customer_id INT,

    store_id INT,
    staff_id INT,

    quantity INT,
    list_price NUMERIC(10,2),
    discount NUMERIC(5,2),

    order_date DATE
);
