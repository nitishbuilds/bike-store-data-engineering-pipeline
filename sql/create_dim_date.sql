CREATE TABLE IF NOT EXISTS warehouse.dim_date (
    date_key INT PRIMARY KEY,
    full_date DATE UNIQUE,
    year INT,
    quarter INT,
    month INT,
    month_name VARCHAR(20),
    day INT,
    day_name VARCHAR(20)
);
