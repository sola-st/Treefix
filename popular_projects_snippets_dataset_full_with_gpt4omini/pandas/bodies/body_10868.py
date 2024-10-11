# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_counting.py
ge = DataFrame().groupby(level=0)
se = Series(dtype=object).groupby(level=0)

# edge case, as this is usually considered float
e = Series(dtype="int64")

tm.assert_series_equal(e, ge.cumcount())
tm.assert_series_equal(e, se.cumcount())
