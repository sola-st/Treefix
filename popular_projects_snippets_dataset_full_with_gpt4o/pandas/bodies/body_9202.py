# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_missing.py

# Nans are represented as -1 in codes
c = Categorical(["a", "b", np.nan, "a"])
tm.assert_index_equal(c.categories, Index(["a", "b"]))
tm.assert_numpy_array_equal(c._codes, np.array([0, 1, -1, 0], dtype=np.int8))
c[1] = np.nan
tm.assert_index_equal(c.categories, Index(["a", "b"]))
tm.assert_numpy_array_equal(c._codes, np.array([0, -1, -1, 0], dtype=np.int8))

# Adding nan to categories should make assigned nan point to the
# category!
c = Categorical(["a", "b", np.nan, "a"])
tm.assert_index_equal(c.categories, Index(["a", "b"]))
tm.assert_numpy_array_equal(c._codes, np.array([0, 1, -1, 0], dtype=np.int8))
