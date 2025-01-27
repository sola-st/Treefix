# Extracted from ./data/repos/pandas/pandas/tests/series/test_missing.py

# NaNs are represented as -1 in labels
s = Series(Categorical(["a", "b", np.nan, "a"]))
tm.assert_index_equal(s.cat.categories, Index(["a", "b"]))
tm.assert_numpy_array_equal(
    s.values.codes, np.array([0, 1, -1, 0], dtype=np.int8)
)
