# Extracted from ./data/repos/pandas/pandas/tests/series/test_api.py
# similarly for .dt
s = Series(date_range("1/1/2015", periods=5))
assert "dt" in dir(s)
assert "str" not in dir(s)
assert "cat" not in dir(s)
