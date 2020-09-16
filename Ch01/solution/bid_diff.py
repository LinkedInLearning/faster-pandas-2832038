import pandas as pd


def second(values):
    """Return second highest value

    >>> second([1, 7, 9, 3, 5])
    7
    """
    top, second = -1, -1
    for value in values:
        if value > top:
            top, second = value, top
        elif value > second:
            second = value
    return second


def median_diff(csv_file):
    df = pd.read_csv(csv_file)
    top1 = df.groupby('id')['price'].max()
    top2 = df.groupby('id')['price'].apply(second)
    diffs = top1 - top2
    return diffs.median()
