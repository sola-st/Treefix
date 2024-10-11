# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# see GH#18311
# assigning series.loc[0] = 4 changed series.dtype to int
series = Series([1, 2, 3], dtype=any_int_numpy_dtype)
series.loc[0] = 4
expected = Series([4, 2, 3], dtype=any_int_numpy_dtype)
tm.assert_series_equal(series, expected)
