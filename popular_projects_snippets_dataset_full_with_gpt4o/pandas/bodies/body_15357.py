# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
value = datetime_series[5]
assert isinstance(value, np.float64)
