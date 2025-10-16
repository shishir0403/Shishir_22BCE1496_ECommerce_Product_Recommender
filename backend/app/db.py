import sqlite3

DB_PATH = "app/database1.db"

def get_connection():
    """Create a new SQLite connection."""
    return sqlite3.connect(DB_PATH)

def initialize_database():
    """Ensure the 'products' table exists before any queries."""
    conn = get_connection()
    cursor = conn.cursor()
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
    print("✅ Database and 'products' table verified/created.")

def get_all_products():
    """Fetch all products from the database."""
    # Ensure table exists before trying to read
    initialize_database()

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, category, price, description, image FROM products")
    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "id": r[0],
            "title": r[1],
            "category": r[2],
            "price": r[3],
            "description": r[4],
            "image": r[5],
        }
        for r in rows
    ]

# Optional: Run a quick check
if __name__ == "__main__":
    initialize_database()
    products = get_all_products()
    print(f"🛒 Found {len(products)} products in the database.")
