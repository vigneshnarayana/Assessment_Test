-- 1: Database Schema
CREATE TABLE transactions (
    transaction_id TEXT PRIMARY KEY,
    customer_id TEXT,
    product_id TEXT,
    quantity INTEGER,
    date TEXT,
    region TEXT,
    total_value REAL,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE products (
    product_id TEXT PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    price REAL
);

CREATE TABLE customers (
    customer_id TEXT PRIMARY KEY,
    customer_name TEXT
);