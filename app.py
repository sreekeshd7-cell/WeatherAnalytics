import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Weather Analytics",
    page_icon="🌦️",
    layout="wide"
)

# Dashboard title
st.title("Weather Data Analytics Dashboard")
st.write("Weather insights collected from multiple Indian cities.")

# Load database
conn = sqlite3.connect("weather.db")

df = pd.read_sql_query(
    "SELECT * FROM weather_records",
    conn
)

conn.close()

# Convert date column
df["recorded_at"] = pd.to_datetime(
    df["recorded_at"],
    format="mixed",
    errors="coerce"
)
# Sidebar
st.sidebar.header("Filters")

cities = sorted(df["city"].unique())

selected_city = st.sidebar.selectbox(
    "Select City",
    ["All Cities"] + cities
)

# Filter data
if selected_city != "All Cities":
    filtered_df = df[df["city"] == selected_city]
else:
    filtered_df = df

# KPI metrics
st.subheader("Weather Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Average Temperature",
    f"{filtered_df['temperature'].mean():.1f} °C"
)

col2.metric(
    "Average Humidity",
    f"{filtered_df['humidity'].mean():.1f} %"
)

col3.metric(
    "Average Wind Speed",
    f"{filtered_df['wind_speed'].mean():.1f} km/h"
)

col4.metric(
    "Total Records",
    len(filtered_df)
)

# Temperature chart
st.subheader("Temperature Comparison")

temperature_chart = px.bar(
    filtered_df,
    x="city",
    y="temperature",
    color="city",
    title="Temperature by City",
    labels={
        "city": "City",
        "temperature": "Temperature (°C)"
    }
)

st.plotly_chart(
    temperature_chart,
    use_container_width=True
)

# Humidity chart
st.subheader("Humidity Comparison")

humidity_chart = px.bar(
    filtered_df,
    x="city",
    y="humidity",
    color="city",
    title="Humidity by City",
    labels={
        "city": "City",
        "humidity": "Humidity (%)"
    }
)

st.plotly_chart(
    humidity_chart,
    use_container_width=True
)

# Wind chart
st.subheader("Wind Speed Comparison")

wind_chart = px.bar(
    filtered_df,
    x="city",
    y="wind_speed",
    color="city",
    title="Wind Speed by City",
    labels={
        "city": "City",
        "wind_speed": "Wind Speed (km/h)"
    }
)

st.plotly_chart(
    wind_chart,
    use_container_width=True
)

# Historical Trend
st.subheader("Historical Temperature Trend")

filtered_df["date"] = filtered_df["recorded_at"].dt.date

daily_data = filtered_df.groupby(
    ["date", "city"]
)["temperature"].mean().reset_index()

trend_chart = px.line(
    daily_data,
    x="date",
    y="temperature",
    color="city",
    markers=True,
    title="Daily Average Temperature",
    labels={
        "date": "Date",
        "temperature": "Average Temperature (°C)",
        "city": "City"
    }
)

st.plotly_chart(
    trend_chart,
    use_container_width=True
)

# Raw data
st.subheader("Weather Records")

st.dataframe(
    filtered_df.sort_values("recorded_at", ascending=False),
    use_container_width=True
)

st.download_button(
    label="Download Weather Data CSV",
    data=filtered_df.to_csv(index=False),
    file_name="weather_data.csv",
    mime="text/csv"
)

# Advanced Analytics

st.divider()

st.header("Advanced Analytics")

# City-wise averages
city_analysis = filtered_df.groupby("city").agg(
    Average_Temperature=("temperature", "mean"),
    Average_Humidity=("humidity", "mean"),
    Average_Wind=("wind_speed", "mean")
).reset_index()

st.subheader("City-wise Weather Analysis")

st.dataframe(
    city_analysis.round(2),
    use_container_width=True
)

# Correlation
st.subheader("Weather Correlation")

correlation = filtered_df[
    ["temperature", "humidity", "wind_speed"]
].corr()

correlation_chart = px.imshow(
    correlation,
    text_auto=True,
    color_continuous_scale="RdBu",
    zmin=-1,
    zmax=1,
    title="Weather Correlation Matrix"
)

st.plotly_chart(
    correlation_chart,
    use_container_width=True
)

# Temperature anomaly
st.subheader("Temperature Anomaly Detection")

mean_temp = filtered_df["temperature"].mean()

std_temp = filtered_df["temperature"].std()

filtered_df["Anomaly"] = (
    (filtered_df["temperature"] > mean_temp + 2 * std_temp)
    |
    (filtered_df["temperature"] < mean_temp - 2 * std_temp)
)

anomaly_data = filtered_df[filtered_df["Anomaly"]]

st.write("Detected unusual temperature readings:")

st.dataframe(
    anomaly_data[
        ["city", "temperature", "recorded_at"]
    ],
    use_container_width=True
)

# Insights
st.subheader("Automated Weather Insights")

hottest = filtered_df.loc[
    filtered_df["temperature"].idxmax()
]

coldest = filtered_df.loc[
    filtered_df["temperature"].idxmin()
]

most_humid = filtered_df.loc[
    filtered_df["humidity"].idxmax()
]

most_windy = filtered_df.loc[
    filtered_df["wind_speed"].idxmax()
]

st.success(
    f"Hottest observation: {hottest['city']} "
    f"({hottest['temperature']}°C)"
)

st.info(
    f"Coldest observation: {coldest['city']} "
    f"({coldest['temperature']}°C)"
)

st.info(
    f"Highest humidity: {most_humid['city']} "
    f"({most_humid['humidity']}%)"
)

st.info(
    f"Highest wind speed: {most_windy['city']} "
    f"({most_windy['wind_speed']} km/h)"
)