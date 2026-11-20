import pandas as pd
import sqlite3

# Connect to database
conn = sqlite3.connect("weather.db")

# Load data
df = pd.read_sql_query(
    "SELECT * FROM weather_records",
    conn
)

conn.close()

# Clean data
df = df.drop_duplicates(
    subset=["city", "recorded_at"]
)

df = df.dropna()

df["recorded_at"] = pd.to_datetime(
    df["recorded_at"]
)

print("\n===== WEATHER ANALYTICS =====")

# 1. Temperature Analysis
print("\nAverage Temperature:")
print(df["temperature"].mean())

print("\nMaximum Temperature:")
print(df["temperature"].max())

print("\nMinimum Temperature:")
print(df["temperature"].min())

# 2. City Comparison
print("\nCity-wise Average Temperature:")

city_temperature = df.groupby("city")["temperature"].mean()

print(city_temperature.sort_values(ascending=False))

# 3. Humidity Analysis
print("\nCity-wise Average Humidity:")

city_humidity = df.groupby("city")["humidity"].mean()

print(city_humidity.sort_values(ascending=False))

# 4. Wind Analysis
print("\nCity-wise Average Wind Speed:")

city_wind = df.groupby("city")["wind_speed"].mean()

print(city_wind.sort_values(ascending=False))

# 5. Correlation Analysis
print("\nCorrelation Matrix:")

correlation = df[
    ["temperature", "humidity", "wind_speed"]
].corr()

print(correlation)

# 6. Detect Temperature Anomalies
mean_temp = df["temperature"].mean()

std_temp = df["temperature"].std()

df["temperature_anomaly"] = (
    df["temperature"] > mean_temp + 2 * std_temp
) | (
    df["temperature"] < mean_temp - 2 * std_temp
)

anomalies = df[df["temperature_anomaly"]]

print("\nTemperature Anomalies:")

print(
    anomalies[
        ["city", "temperature", "recorded_at"]
    ]
)

# 7. Automated Insights
hottest_city = city_temperature.idxmax()

coldest_city = city_temperature.idxmin()

most_humid_city = city_humidity.idxmax()

windy_city = city_wind.idxmax()

print("\n===== AUTOMATED INSIGHTS =====")

print(f"Hottest city: {hottest_city}")

print(f"Coldest city: {coldest_city}")

print(f"Most humid city: {most_humid_city}")

print(f"Windiest city: {windy_city}")

print("\nAnalysis Completed!")