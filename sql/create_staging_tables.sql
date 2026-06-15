CREATE TABLE IF NOT EXISTS staging.stg_brands (
    brand_id INT PRIMARY KEY,
    brand_name VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS staging.stg_categories (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS staging.stg_customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    phone VARCHAR(50),
    email VARCHAR(255),
    street VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(50),
    zip_code VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS staging.stg_orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_status INT,
    order_date DATE,
    required_date DATE,
    shipped_date DATE,
    store_id INT,
    staff_id INT
);

CREATE TABLE IF NOT EXISTS staging.stg_order_items (
    order_id INT,
    item_id INT,
    product_id INT,
    quantity INT,
    list_price NUMERIC(10,2),
    discount NUMERIC(5,2)
);

CREATE TABLE IF NOT EXISTS staging.stg_products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(255),
    brand_id INT,
    category_id INT,
    model_year INT,
    list_price NUMERIC(10,2)
);

CREATE TABLE IF NOT EXISTS staging.stg_staffs (
    staff_id INT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(255),
    phone VARCHAR(50),
    active INT,
    store_id INT,
    manager_id INT
);

CREATE TABLE IF NOT EXISTS staging.stg_stocks (
    store_id INT,
    product_id INT,
    quantity INT
);

CREATE TABLE IF NOT EXISTS staging.stg_stores (
    store_id INT PRIMARY KEY,
    store_name VARCHAR(255),
    phone VARCHAR(50),
    email VARCHAR(255),
    street VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(50),
    zip_code VARCHAR(20)
);
