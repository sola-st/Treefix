# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
series = Series(list(date_range("1/1/2000", periods=10)))
assert series.dtype == "M8[ns]"
