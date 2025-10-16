import sqlite3

DB_PATH = "database1.db"

def seed_data():
    data = [
        ("Wireless Noise-Cancelling Headphones", "Electronics", 199.99, "Over-ear, 30h battery, active noise cancellation", "https://plus.unsplash.com/premium_photo-1679513691474-73102089c117?ixlib=rb-4.1.0&auto=format&fit=crop&q=80&w=1113"),
        ("Smart Fitness Watch", "Wearables", 149.99, "Tracks heart rate, sleep, and workouts", "https://images.unsplash.com/photo-1587400519568-1fe0329bfb2e?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=1170"),
        ("4K Action Camera", "Electronics", 299.99, "Waterproof up to 30m, 60fps recording", "https://images.unsplash.com/photo-1603720913661-76d1053714e2?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=1170"),
        ("Ergonomic Office Chair", "Furniture", 259.99, "Adjustable lumbar support and breathable mesh", "https://images.unsplash.com/photo-1688578735427-994ecdea3ea4?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=687"),
        ("Bluetooth Portable Speaker", "Audio", 89.99, "10h battery life, deep bass sound", "https://images.unsplash.com/photo-1589256469067-ea99122bbdc4?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=1074"),
        ("Mechanical Keyboard", "Accessories", 129.99, "RGB backlight, hot-swappable switches", "https://images.unsplash.com/photo-1602025882379-e01cf08baa51?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=1170"),
        ("Noise-Isolating Earbuds", "Audio", 79.99, "Compact design, clear sound", "https://images.unsplash.com/photo-1590658268037-6bf12165a8df"),
        ("Gaming Laptop", "Computers", 1199.99, "RTX 4070, 16GB RAM, 1TB SSD", "https://images.unsplash.com/photo-1611078489935-0cb964de46d6?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=1074"),
        ("Smart Home Speaker", "Smart Devices", 129.99, "Voice assistant, multi-room audio", "https://images.unsplash.com/photo-1579208570378-8c970854bc23"),
        ("Standing Desk", "Furniture", 399.99, "Adjustable height, modern design", "https://images.unsplash.com/photo-1622126756000-9fb7f6ed9f06?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=1170"),
        ("Wireless Mouse", "Accessories", 49.99, "Silent clicks, ergonomic shape", "https://images.unsplash.com/photo-1611078489935-0cb964de46d6?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=1074"),
        ("Curved 27-inch Monitor", "Computers", 349.99, "144Hz refresh rate, 2K resolution", "https://images.unsplash.com/photo-1666771410140-0573b232426e?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=1074" ),
        ("Portable Power Bank", "Electronics", 59.99, "20000mAh fast charging battery", "https://images.unsplash.com/photo-1687007081819-ac1bb40d5674?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=1074"),
        ("LED Desk Lamp", "Furniture", 69.99, "Touch control, dimmable lighting", "https://images.unsplash.com/photo-1586023492125-27b2c045efd7"),
    ]

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Ensure the table exists (in case create_table.py wasn’t run)
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

    # Clear existing data (optional)
    cursor.execute("DELETE FROM products")

    # Insert all records
    cursor.executemany("""
        INSERT INTO products (title, category, price, description, image)
        VALUES (?, ?, ?, ?, ?);
    """, data)

    conn.commit()
    conn.close()
    print(f"✅ Database seeded successfully with sample products! in {DB_PATH}")


if __name__ == "__main__":
    seed_data()
