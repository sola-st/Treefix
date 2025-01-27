# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_indexing.py
# Case: taking a slice of a Series + afterwards modifying the subset
s = Series([1, 2, 3], index=["a", "b", "c"])
s_orig = s.copy()

subset = s[:]
assert np.shares_memory(subset.values, s.values)

subset.iloc[0] = 0

if using_copy_on_write:
    assert not np.shares_memory(subset.values, s.values)

expected = Series([0, 2, 3], index=["a", "b", "c"])
tm.assert_series_equal(subset, expected)

if using_copy_on_write:
    # original parent series is not modified (CoW)
    tm.assert_series_equal(s, s_orig)
else:
    # original parent series is actually updated
    assert s.iloc[0] == 0
