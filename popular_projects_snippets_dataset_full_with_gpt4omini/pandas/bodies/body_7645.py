# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_get_set.py
# Test MultiIndex.dtypes with non-unique level names (# GH45174)
result = MultiIndex.from_product(
    [
        [1, 2, 3],
        ["a", "b", "c"],
        pd.date_range("20200101", periods=2, tz="UTC"),
    ],
    names=["A", "A", "A"],
).dtypes
expected = pd.Series(
    [np.dtype("int64"), np.dtype("O"), DatetimeTZDtype(tz="utc")],
    index=["A", "A", "A"],
)
tm.assert_series_equal(result, expected)
