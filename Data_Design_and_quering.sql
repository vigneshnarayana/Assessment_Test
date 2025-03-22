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

-- SQL Queries
-- 1.Total sales value by region:
SELECT region, SUM(total_value) AS total_sales
FROM sales
GROUP BY region;
-- Top 5 products by total sales value:
SELECT product_name, SUM(total_value) AS total_sales
FROM sales
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 5;
-- Monthly sales trends:
SELECT strftime('%Y-%m', date) AS month, SUM(total_value) AS total_sales
FROM sales
GROUP BY month
ORDER BY month;

Performance Optimization
-- 2. Optimize SQL Queries
CREATE INDEX idx_date ON sales(date);
CREATE INDEX idx_region ON sales(region);