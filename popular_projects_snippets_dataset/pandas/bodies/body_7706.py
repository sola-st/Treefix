# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_isin.py
idx = MultiIndex.from_arrays([["foo", "bar"], [1.0, np.nan]])
tm.assert_numpy_array_equal(idx.isin([("bar", np.nan)]), np.array([False, True]))
tm.assert_numpy_array_equal(
    idx.isin([("bar", float("nan"))]), np.array([False, True])
)
