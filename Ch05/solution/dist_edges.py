"""Calculate the minimal and maximal distance driven from the data at
    taxi.csv.xz
Consume as little memory as possible and don't load more than 50,000 rows at a
time.
"""

import pandas as pd

min_dist, max_dist = float('inf'), float('-inf')
dfs = pd.read_csv('taxi.csv.xz', usecols=['trip_distance'], chunksize=50_000)
for df in dfs:
    desc = df['trip_distance'].describe()
    min_dist = min(min_dist, desc['min'])
    max_dist = max(max_dist, desc['max'])

print('min', min_dist, 'max', max_dist)
