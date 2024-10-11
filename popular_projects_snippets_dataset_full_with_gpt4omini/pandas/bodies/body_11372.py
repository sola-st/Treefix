# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_indexing.py
s = Series([1, 2, 3], index=["a", "b", "c"])
s_orig = s.copy()

s2 = method(s)

# we always return new objects, regardless of CoW or not
assert s2 is not s

# and those trigger CoW when mutated
s2.iloc[0] = 0
if using_copy_on_write:
    tm.assert_series_equal(s, s_orig)
else:
    assert s.iloc[0] == 0
