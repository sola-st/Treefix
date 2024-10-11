# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_interval_array_equal.py
arr = interval_range(**kwargs).values
tm.assert_interval_array_equal(arr, arr)
