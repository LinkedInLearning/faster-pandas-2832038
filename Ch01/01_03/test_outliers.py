import numpy as np
import pandas as pd

from outliers import find_outliers


def gen_data(size, num_outliers):
    """Generate data in with size element containint num_outliers outliers.
    Returns the data and the outliers.
    """
    regular = np.random.randint(50, 60, size-num_outliers)
    low = np.random.randint(1, 10, num_outliers//2)
    high = np.random.randint(100, 110, num_outliers-len(low))

    data = np.concatenate([regular, low, high])
    np.random.shuffle(data)
    return pd.Series(data), pd.Series(np.concatenate([low, high]))


def test_bench_outliers(benchmark):
    size = 10_000  # Usual size of data
    num_outliers = 5  # Usual number of outliers
    data, expected = gen_data(size, num_outliers)
    indices = benchmark(find_outliers, data)
    outliers = data.loc[indices]
    assert set(expected) == set(outliers), 'bad result'
