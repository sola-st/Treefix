# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_series_equal.py
s1 = Series([1, 2, 3], index=["a", "b", "c"])
s2 = Series([1, 2, 3], index=["c", "b", "a"])

if check_index:  # Do not ignore index.
    with pytest.raises(AssertionError, match="Series.index are different"):
        tm.assert_series_equal(s1, s2, check_index=check_index)
else:
    _assert_series_equal_both(s1, s2, check_index=check_index)
