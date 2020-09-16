"""Using vaex, calculate the mean taxi ride distance in "taxi.csv.xz" per
VendorID.
"""

import vaex

df = vaex.read_csv('taxi.csv.xz')
out = df.groupby('VendorID', vaex.agg.mean(df['trip_distance']))
print(out)
