import sqlite3

DB_PATH = "database1.db"

def create_products_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create products table with all required fields
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL,
            description TEXT,
            image TEXT
        );
    """)

    conn.commit()
    conn.close()
    print("✅ Table 'products' created successfully!")


if __name__ == "__main__":
    create_products_table()
