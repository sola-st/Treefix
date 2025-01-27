# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH#44923
result = Series(["0", "1", "2"], dtype=any_int_dtype)
expected = Series([0, 1, 2], dtype=any_int_dtype)
tm.assert_series_equal(result, expected)
