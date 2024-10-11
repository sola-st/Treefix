# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_concat.py
# GH 13247
dims = frame_or_series(dtype=object).ndim

dfs = [
    frame_or_series(np.array([1], dtype=dt, ndmin=dims)),
    frame_or_series(np.array([np.nan], dtype=dt, ndmin=dims)),
    frame_or_series(np.array([5], dtype=dt, ndmin=dims)),
]
x = concat(dfs)
assert x.values.dtype == dt
