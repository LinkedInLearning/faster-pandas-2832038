"""Find how many rides in 2016 were in the afternoon of weekend or holiday.

- Afternoon: Between noon to 6pm
- Weekend: Friday or Saturday
- Holiday: See holidays_2016 below
"""

from calendar import SATURDAY, SUNDAY

import pandas as pd

# 2016 public holidays
holidays_2016 = pd.to_datetime([
    '2016-01-01',  # new year
    '2016-01-18',  # MLK
    '2016-05-30',  # memorial
    '2016-07-04',  # independence
    '2016-09-05',  # labor
    '2016-11-11',  # veterans
    '2016-11-24',  # thanksgiving
    '2016-12-26',  # christmas
])


def load_df(file_name):
    """Load data from CSV to DataFrame"""
    return pd.read_csv(
        file_name,
        parse_dates={'time': ['Checkout Date', 'Checkout Time']},
    )


def vacation_rides(df):
    """Return only rows that are in holiday afternoon"""
    mask_2016 = df['time'].dt.year == 2016

    holiday_mask = (
        (df['time'].dt.floor('d').isin(holidays_2016)) |
        (df['time'].dt.weekday.isin([SATURDAY, SUNDAY]))
    )

    afternoon_mask = (df['time'].dt.hour >= 12) & (df['time'].dt.hour < 18)

    return df[mask_2016 & holiday_mask & afternoon_mask]
