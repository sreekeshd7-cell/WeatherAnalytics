import pandas as pd
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt

conn = sqlite3.connect("weather.db")

df = pd.read_sql_query(
    "SELECT temperature, humidity, wind_speed FROM weather_records",
    conn
)

conn.close()

correlation = df.corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    vmin=-1,
    vmax=1
)

plt.title("Weather Variable Correlation")

plt.show()