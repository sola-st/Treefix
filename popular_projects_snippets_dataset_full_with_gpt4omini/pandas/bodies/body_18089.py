# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_series_equal.py
data = range(3)
s1 = Series(data)

s2 = Series(data, **kwargs)
_assert_not_series_equal_both(s1, s2)
