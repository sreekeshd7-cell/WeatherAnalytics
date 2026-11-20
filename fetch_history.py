import requests
import pandas as pd
import sqlite3

cities = {
    "Chandigarh": (30.7333, 76.7794),
    "Delhi": (28.6139, 77.2090),
    "Mumbai": (19.0760, 72.8777),
    "Bengaluru": (12.9716, 77.5946),
    "Chennai": (13.0827, 80.2707)
}

records = []

for city, coordinates in cities.items():

    latitude, longitude = coordinates

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "past_days": 7,
        "timezone": "Asia/Kolkata"
    }

    try:
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()

        data = response.json()
        hourly = data["hourly"]

        times = pd.to_datetime(hourly["time"])

        now = pd.Timestamp.now(tz="Asia/Kolkata").tz_localize(None)
        cutoff = now - pd.Timedelta(days=7)

        for i, time in enumerate(times):

            if cutoff <= time <= now:

                records.append({
                    "city": city,
                    "temperature": hourly["temperature_2m"][i],
                    "humidity": hourly["relative_humidity_2m"][i],
                    "wind_speed": hourly["wind_speed_10m"][i],
                    "recorded_at": str(time)
                })

        print(f"Data fetched successfully for {city}")

    except Exception as e:
        print(f"Error fetching {city}: {e}")


df = pd.DataFrame(records)

print("\nFetched Records:", len(df))

conn = sqlite3.connect("weather.db")

before = pd.read_sql_query(
    "SELECT COUNT(*) AS total FROM weather_records",
    conn
)["total"][0]

query = """
INSERT OR IGNORE INTO weather_records
(city, temperature, humidity, wind_speed, recorded_at)
VALUES (?, ?, ?, ?, ?)
"""

conn.executemany(
    query,
    df.itertuples(index=False, name=None)
)

conn.commit()

after = pd.read_sql_query(
    "SELECT COUNT(*) AS total FROM weather_records",
    conn
)["total"][0]

conn.close()

print("New records inserted:", after - before)
print("Total database records:", after)

df.to_csv("weather_history.csv", index=False)

print("\nHistorical weather collection completed!")