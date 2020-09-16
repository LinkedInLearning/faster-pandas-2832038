"""Using "bikes.db", find the 5 bikes (using "bike_id") that has the biggest
90% quantile of ride duration in the first quarter of 2017.
"""
import sqlite3

import pandas as pd

conn = sqlite3.connect('bikes.db')
sql = '''
SELECT bike_id, duration
FROM bike_rides
WHERE year == 2017 AND month < 4
'''
df = pd.read_sql(sql, conn)
out = df.groupby('bike_id')['duration'].quantile(.9)
print(out.sort_values(ascending=False)[:5])
