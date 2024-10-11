# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_reset_index.py
# GH 19602 - Preserve dtype on empty Series with MultiIndex
idx = MultiIndex.from_product([[0, 1], [0.5, 1.0], array])
result = Series(dtype=object, index=idx)[:0].reset_index().dtypes
expected = Series(
    {"level_0": np.int64, "level_1": np.float64, "level_2": dtype, 0: object}
)
tm.assert_series_equal(result, expected)
