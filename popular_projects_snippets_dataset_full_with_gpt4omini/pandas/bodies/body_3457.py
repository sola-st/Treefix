# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reset_index.py
# GH 19602 - Preserve dtype on empty DataFrame with MultiIndex
idx = MultiIndex.from_product([[0, 1], [0.5, 1.0], array])
result = DataFrame(index=idx)[:0].reset_index().dtypes
expected = Series({"level_0": np.int64, "level_1": np.float64, "level_2": dtype})
tm.assert_series_equal(result, expected)
