# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_indexing.py
datetime_series[datetime_series.index[5]] = np.NaN
datetime_series[[1, 2, 17]] = np.NaN
datetime_series[6] = np.NaN
assert np.isnan(datetime_series[6])
assert np.isnan(datetime_series[2])
datetime_series[np.isnan(datetime_series)] = 5
assert not np.isnan(datetime_series[2])
