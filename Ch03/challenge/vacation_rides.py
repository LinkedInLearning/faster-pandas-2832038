"""Find how many rides in 2016 were in the afternoon of weekend or holiday.

- Afternoon: Between noon to 6pm
- Weekend: Saturday or Sunday
- Holiday: See holidays_2016 below
"""

import pandas as pd

# 2016 public holidays
holidays_2016 = [
    '2016-01-01',  # new year
    '2016-01-18',  # MLK
    '2016-05-30',  # memorial
    '2016-07-04',  # independence
    '2016-09-05',  # labor
    '2016-11-11',  # veterans
    '2016-11-24',  # thanksgiving
    '2016-12-26',  # christmas
]


def load_df(file_name):
    """Load data from CSV to DataFrame"""
    return pd.read_csv(file_name)


def is_2016(s):
    ts = pd.to_datetime(s)

    return ts.year == 2016


def is_weekend(s):
    """Check that s in a weekend day"""
    ts = pd.to_datetime(s)

    return ts.day_name() == 'Saturday' or ts.day_name() == 'Sunday'


def is_holiday(s):
    """Check that s (e.g. '10/26/2014') is a holiday"""
    ts = pd.to_datetime(s)

    day = ts.strftime('%Y-%m-%d')  # holidays_2016 format
    return day in holidays_2016


def is_afternoon(s):
    """Check that s (e.g. '13:12:00' is in the afternoon"""
    ts = pd.to_datetime(s)

    return ts.hour >= 12 and ts.hour < 18


def vacation_rides(df):
    """Return only rows that are in holiday afternoon"""
    result = pd.DataFrame()
    for _, row in df.iterrows():
        date, time = row['Checkout Date'], row['Checkout Time']
        if not is_2016(date):
            continue

        if (is_holiday(date) or is_weekend(date)) and is_afternoon(time):
            result = result.append(row, ignore_index=True)

    return result
