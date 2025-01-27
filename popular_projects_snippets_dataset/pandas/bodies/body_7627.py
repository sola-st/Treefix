# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
# https://github.com/pandas-dev/pandas/issues/26944
idx = MultiIndex.from_product(
    [
        date_range("2019-01-01T00:15:33", periods=100, freq="H", name="date"),
        ["x"],
        [3],
    ]
)
df = pd.DataFrame({"foo": np.arange(len(idx))}, idx)
result = df.loc[pd.IndexSlice["2019-1-2":, "x", :], "foo"]
qidx = MultiIndex.from_product(
    [
        date_range(
            start="2019-01-02T00:15:33",
            end="2019-01-05T03:15:33",
            freq="H",
            name="date",
        ),
        ["x"],
        [3],
    ]
)
should_be = pd.Series(data=np.arange(24, len(qidx) + 24), index=qidx, name="foo")
tm.assert_series_equal(result, should_be)
