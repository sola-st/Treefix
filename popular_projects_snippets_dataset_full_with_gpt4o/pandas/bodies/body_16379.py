# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH#43017
result = Series(index=[0], dtype="int64")
expected = Series(np.nan, index=[0], dtype="float64")
tm.assert_series_equal(result, expected)
