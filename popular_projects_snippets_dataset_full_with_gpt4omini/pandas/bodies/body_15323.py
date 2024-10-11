# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
# GH#34860
arr = date_range("1/1/2008", "1/1/2009")
ser = arr.to_series()
result = ser["2008"]

rng = date_range(start="2008-01-01", end="2008-12-31")
expected = Series(rng, index=rng)

tm.assert_series_equal(result, expected)
