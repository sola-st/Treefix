# Extracted from ./data/repos/pandas/pandas/tests/series/test_api.py
# similar to cat and str
s = Series(date_range("1/1/2015", periods=5)).astype("category")
assert "cat" in dir(s)
assert "str" not in dir(s)
assert "dt" in dir(s)  # as it is a datetime categorical
