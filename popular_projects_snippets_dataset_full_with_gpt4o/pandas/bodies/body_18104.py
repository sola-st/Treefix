# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_series_equal.py
# https://github.com/pandas-dev/pandas/issues/35715
left = Series([1, 2, 3], dtype="Int64")
right = Series([1, 2, 3], dtype=right_dtype)
tm.assert_series_equal(left, right, check_dtype=False)
