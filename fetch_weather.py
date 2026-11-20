import requests
import sqlite3
from datetime import datetime

cities = {
    "Chandigarh": (30.7333, 76.7794),
    "Delhi": (28.6139, 77.2090),
    "Mumbai": (19.0760, 72.8777),
    "Bengaluru": (12.9716, 77.5946),
    "Chennai": (13.0827, 80.2707)
}

url = "https://api.open-meteo.com/v1/forecast"

records = []

for city, coordinates in cities.items():

    latitude, longitude = coordinates

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "timezone": "Asia/Kolkata"
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=15
        )

        response.raise_for_status()

        data = response.json()
        weather = data["current"]

        record = (
            city,
            weather["temperature_2m"],
            weather["relative_humidity_2m"],
            weather["wind_speed_10m"],
            weather["time"]
        )

        records.append(record)

        print(f"Collected weather for {city}")

    except Exception as e:
        print(f"Failed to collect {city}: {e}")

# Connect to database
conn = sqlite3.connect("weather.db")

cursor = conn.cursor()

# Insert records
cursor.executemany("""
INSERT OR IGNORE INTO weather_records
(city, temperature, humidity, wind_speed, recorded_at)
VALUES (?, ?, ?, ?, ?)
""", records)

conn.commit()

conn.close()

print("\nCollection completed!")
print("Records collected:", len(records))
print("Time:", datetime.now())