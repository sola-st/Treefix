# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_set_value.py
idx = datetime_series.index[10]
res = datetime_series._set_value(idx, 0)
assert res is None
assert datetime_series[idx] == 0
