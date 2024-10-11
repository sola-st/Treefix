# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_bin_groupby.py
values = np.array([1, 2, 3, 4, 5, 6], dtype=np.int64)
result = lib.generate_bins_dt64(values, binner, closed=closed)
tm.assert_numpy_array_equal(result, expected)
