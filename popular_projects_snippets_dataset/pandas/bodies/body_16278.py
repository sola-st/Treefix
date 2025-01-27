# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# see GH#16524: test conversion of Series to Categorical
series = Series(["a", "b", "c"])

result = Series(series, dtype="category")
expected = Series(["a", "b", "c"], dtype="category")

tm.assert_series_equal(result, expected)
