import sqlite3
import pandas as pd

conn = sqlite3.connect("weather.db")

query = """
SELECT
    city,
    temperature,
    humidity,
    wind_speed,
    recorded_at
FROM weather_records
ORDER BY recorded_at
"""

df = pd.read_sql_query(query, conn)

conn.close()

df["recorded_at"] = pd.to_datetime(df["recorded_at"])

print("\n--- COMPLETE HISTORICAL DATA ---")
print(df)

print("\n--- DAILY TEMPERATURE AVERAGE ---")

daily_temperature = df.groupby(
    [df["recorded_at"].dt.date, "city"]
)["temperature"].mean()

print(daily_temperature)

print("\n--- DAILY HUMIDITY AVERAGE ---")

daily_humidity = df.groupby(
    [df["recorded_at"].dt.date, "city"]
)["humidity"].mean()

print(daily_humidity)

print("\n--- CITY-WISE TEMPERATURE SUMMARY ---")

city_summary = df.groupby("city").agg(
    Average_Temperature=("temperature", "mean"),
    Maximum_Temperature=("temperature", "max"),
    Minimum_Temperature=("temperature", "min"),
    Average_Humidity=("humidity", "mean"),
    Average_Wind_Speed=("wind_speed", "mean")
)

print(city_summary)

print("\n--- DATA COLLECTION COUNT ---")

print(df.groupby("city").size())

print("\nHistorical analysis completed!")
