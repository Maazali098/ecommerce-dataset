import sqlite3
import csv

# Full path to your products.csv file
csv_file_path = r"C:\Users\maaz mohammad\OneDrive\Pictures\screenshots\Desktop\think41-ecommerce-app\backend folder\products.csv"

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Step 1: Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        category TEXT,
        price REAL,
        stock INTEGER
    )
''')

# Step 2: Load CSV and insert data
with open(csv_file_path, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    products = [(row['id'], row['name'], row['category'], row['price'], row['stock']) for row in reader]

cursor.executemany('INSERT INTO products (id, name, category, price, stock) VALUES (?, ?, ?, ?, ?)', products)
conn.commit()

# Step 3: Verify by fetching some rows
cursor.execute('SELECT * FROM products LIMIT 5')
rows = cursor.fetchall()

print("Sample data from database:")
for row in rows:
    print(row)

conn.close()