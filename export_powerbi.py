import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("weather.db")

# Load weather records
df = pd.read_sql_query("""
SELECT
    city,
    temperature,
    humidity,
    wind_speed,
    recorded_at
FROM weather_records
""", conn)

conn.close()

# Remove duplicate records
df = df.drop_duplicates(
    subset=["city", "recorded_at"]
)

# Remove missing values
df = df.dropna()

# Convert date column
df["recorded_at"] = pd.to_datetime(
    df["recorded_at"]
)

# Export
df.to_csv(
    "powerbi_weather.csv",
    index=False
)

print("Power BI dataset exported successfully!")
print(df.head())
print("\nTotal records:", len(df))