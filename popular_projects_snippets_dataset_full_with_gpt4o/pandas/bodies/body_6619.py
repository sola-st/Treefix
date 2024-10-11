# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_range.py

idx = RangeIndex(5, name="Foo")
result = idx[1:4]

# test 0th element
tm.assert_index_equal(idx[0:4], result.insert(0, idx[0]), exact="equiv")

# GH 18295 (test missing)
expected = Index([0, np.nan, 1, 2, 3, 4], dtype=np.float64)
for na in [np.nan, None, pd.NA]:
    result = RangeIndex(5).insert(1, na)
    tm.assert_index_equal(result, expected)

result = RangeIndex(5).insert(1, pd.NaT)
expected = Index([0, pd.NaT, 1, 2, 3, 4], dtype=object)
tm.assert_index_equal(result, expected)
