# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
idx = np.int64(5)
assert datetime_series[idx] == datetime_series[5]
