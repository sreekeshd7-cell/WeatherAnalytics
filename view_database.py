import sqlite3
import pandas as pd

conn = sqlite3.connect("weather.db")

query = """
SELECT
    city,
    COUNT(*) AS total_records,
    MIN(recorded_at) AS first_record,
    MAX(recorded_at) AS last_record
FROM weather_records
GROUP BY city
ORDER BY city
"""

df = pd.read_sql_query(query, conn)

print(df)

conn.close()