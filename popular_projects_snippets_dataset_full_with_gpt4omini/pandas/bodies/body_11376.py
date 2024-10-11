# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_indexing.py
s = Series([1, 2, 3], index=["a", "b", "c"])
s_orig = s.copy()
s2 = s[:]

assert np.shares_memory(s.values, s2.values)

del s2["a"]

assert not np.shares_memory(s.values, s2.values)
tm.assert_series_equal(s, s_orig)
tm.assert_series_equal(s2, s_orig[["b", "c"]])

# modifying s2 doesn't need copy on write (due to `del`, s2 is backed by new array)
values = s2.values
s2.loc["b"] = 100
assert values[0] == 100
