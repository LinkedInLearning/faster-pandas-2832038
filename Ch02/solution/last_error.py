"""Find last time we had error in logs"""

import sqlite3
from contextlib import closing

import pandas as pd


def last_error_time(df):
    """Find last time there's an error in df"""
    return df[df['status_code'] >= 400]['time'].max()


def load_df(db_file):
    """Load DataFrame from database"""
    conn = sqlite3.connect(db_file, detect_types=sqlite3.PARSE_DECLTYPES)
    with closing(conn):
        return pd.read_sql('SELECT * FROM logs', conn)
