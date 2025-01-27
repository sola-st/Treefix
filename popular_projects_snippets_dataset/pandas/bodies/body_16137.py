# Extracted from ./data/repos/pandas/pandas/tests/series/test_api.py
full_series = Series(index=[1], dtype=dtype)
assert not full_series.empty
