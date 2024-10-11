# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_concat.py
with catch_warnings(record=True):
    dims = pdt().ndim
    dfs = [
        pdt(np.array([1], dtype=dt, ndmin=dims)),
        pdt(np.array([np.nan], ndmin=dims)),
        pdt(np.array([5], dtype=dt, ndmin=dims)),
    ]
    x = concat(dfs)
    assert x.values.dtype == "float64"
