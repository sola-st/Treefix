# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_indexing.py
# Case: creating a subset using multiple, chained getitem calls using views
# still needs to guarantee proper CoW behaviour
s = Series([1, 2, 3], index=["a", "b", "c"])
s_orig = s.copy()

# modify subset -> don't modify parent
subset = method(s)
subset.iloc[0] = 0
if using_copy_on_write:
    tm.assert_series_equal(s, s_orig)
else:
    assert s.iloc[0] == 0

# modify parent -> don't modify subset
subset = s.iloc[0:3].iloc[0:2]
s.iloc[0] = 0
expected = Series([1, 2], index=["a", "b"])
if using_copy_on_write:
    tm.assert_series_equal(subset, expected)
else:
    assert subset.iloc[0] == 0
