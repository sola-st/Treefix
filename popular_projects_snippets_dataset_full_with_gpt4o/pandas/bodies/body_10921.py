# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_nunique.py
# GH 12553
data = Series(name="name", dtype=object)
result = data.groupby(level=0).nunique()
expected = Series(name="name", dtype="int64")
tm.assert_series_equal(result, expected)
