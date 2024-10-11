# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_get_set.py
# Test MultiIndex.dtypes (# GH38580 )
idx_multitype = MultiIndex.from_product(
    [
        [1, 2, 3],
        ["a", "b", "c"],
        pd.date_range("20200101", periods=2, tz="UTC"),
    ],
)
expected = pd.Series(
    {
        "level_0": np.dtype("int64"),
        "level_1": np.dtype("O"),
        "level_2": DatetimeTZDtype(tz="utc"),
    }
)
tm.assert_series_equal(expected, idx_multitype.dtypes)
