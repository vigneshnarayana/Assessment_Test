# 1. Extract Data from JSON

import pandas as pd
import json

with open('sales_data.json', 'r') as file:
    data = json.load(file)
df = pd.DataFrame(data)

# 2. Transform Data
# 	2.a Flatten the nested product object:

df = pd.concat([df.drop(['product'], axis=1), df['product'].apply(pd.Series)], axis=1)
df.rename(columns={'id': 'product_id', 'name': 'product_name'}, inplace=True)
	# 2.b Standardize date format
	
df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
	# 2.c Calculate total_value:
df['total_value'] = df['quantity'] * df['price']
	
	# 2.d Handle missing or invalid data:
df['customer_id'].fillna('Unknown', inplace=True)
df['quantity'] = df['quantity'].apply(lambda x: max(x, 0)) 
	
	# 2.e Load Data into a Relational Database:
import sqlite3

#SQLite database 
conn = sqlite3.connect('sales.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    transaction_id TEXT PRIMARY KEY,
    customer_id TEXT,
    product_id TEXT,
    product_name TEXT,
    category TEXT,
    price REAL,
    quantity INTEGER,
    date TEXT,
    region TEXT,
    total_value REAL
)
''')


# Insert data into the table
df.to_sql('sales', conn, if_exists='replace', index=False)

""" Data Quality Checks"""

# Check for duplicate transaction_ids
if df['transaction_id'].duplicated().any():
    print("Duplicate transaction_ids found!")
# Log anomalies:
with open('anomalies.log', 'w') as log_file:
    if df['customer_id'].isnull().any():
        log_file.write("Missing customer_id found.\n")
    if (df['quantity'] < 0).any():
        log_file.write("Negative quantity found.\n")
        
# Performance Optimization

# 1.Optimize Data Loading
df.to_sql('sales', conn, if_exists='replace', index=False, chunksize=1000)

