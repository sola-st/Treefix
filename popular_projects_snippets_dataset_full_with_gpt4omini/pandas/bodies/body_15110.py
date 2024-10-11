# Extracted from ./data/repos/pandas/pandas/tests/base/test_value_counts.py
klass = index_or_series
s_values = ["a", "b", "b", "b", "b", "c", "d", "d", "a", "a"]
s = klass(s_values)
expected = Series([4, 3, 2, 1], index=["b", "a", "d", "c"])
tm.assert_series_equal(s.value_counts(), expected)

if isinstance(s, Index):
    exp = Index(np.unique(np.array(s_values, dtype=np.object_)))
    tm.assert_index_equal(s.unique(), exp)
else:
    exp = np.unique(np.array(s_values, dtype=np.object_))
    tm.assert_numpy_array_equal(s.unique(), exp)

assert s.nunique() == 4
# don't sort, have to sort after the fact as not sorting is
# platform-dep
hist = s.value_counts(sort=False).sort_values()
expected = Series([3, 1, 4, 2], index=list("acbd")).sort_values()
tm.assert_series_equal(hist, expected)

# sort ascending
hist = s.value_counts(ascending=True)
expected = Series([1, 2, 3, 4], index=list("cdab"))
tm.assert_series_equal(hist, expected)

# relative histogram.
hist = s.value_counts(normalize=True)
expected = Series([0.4, 0.3, 0.2, 0.1], index=["b", "a", "d", "c"])
tm.assert_series_equal(hist, expected)
