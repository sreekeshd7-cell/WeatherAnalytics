import sqlite3

conn = sqlite3.connect("weather.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS weather_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT NOT NULL,
    temperature REAL,
    humidity REAL,
    wind_speed REAL,
    recorded_at TEXT,
    UNIQUE(city, recorded_at)
)
""")

conn.commit()

conn.close()

print("Database and table created successfully!")