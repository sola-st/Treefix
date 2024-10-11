# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_get_set.py
# Test MultiIndex.dtypes (# Gh37062)
idx_multitype = MultiIndex.from_product(
    [[1, 2, 3], ["a", "b", "c"], pd.date_range("20200101", periods=2, tz="UTC")],
    names=["int", "string", "dt"],
)
expected = pd.Series(
    {
        "int": np.dtype("int64"),
        "string": np.dtype("O"),
        "dt": DatetimeTZDtype(tz="utc"),
    }
)
tm.assert_series_equal(expected, idx_multitype.dtypes)
