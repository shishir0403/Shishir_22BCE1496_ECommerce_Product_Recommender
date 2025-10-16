import sqlite3

conn = sqlite3.connect("database1.db")
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM products")
count = cursor.fetchone()[0]
print("🧾 Total products in DB:", count)
conn.close()