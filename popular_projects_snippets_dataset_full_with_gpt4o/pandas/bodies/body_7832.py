# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_period.py
index = period_range(freq="A", start="1/1/2001", end="12/1/2009")
series = Series(1, index=index)
assert isinstance(series, Series)
