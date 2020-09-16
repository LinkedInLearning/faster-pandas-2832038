"""What is the median trip duration in 2017, only in active kiosks?

- Trip data in austin-bikes.csv.xz
- Kiosk status data in austin-kiosk.csv
"""

import pandas as pd

bike_df = pd.read_csv('austin-bikes.csv.xz', low_memory=False)

# Set index to 'Kiosk ID' for faster merge
kiosk_df = pd.read_csv('austin-kiosk.csv', index_col='Kiosk ID')
df = pd.merge(
    bike_df, kiosk_df, left_on='Checkout Kiosk ID', right_index=True)

# Use query for selecting data
active_2017 = df.query(
    '`Kiosk Status` == "active" & Year == 2017 & `Trip Duration Minutes` > 0')

# Use built-in median
print(active_2017['Trip Duration Minutes'].median())
