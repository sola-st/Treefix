# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
# https://github.com/pandas-dev/pandas/issues/21390
midx = MultiIndex.from_product(
    [
        Categorical(["a", "b", "c"]),
        Categorical(date_range("2012-01-01", periods=3, freq="H")),
    ]
)
df = DataFrame({"a": range(len(midx))}, index=midx)
df2 = df.iloc[[0, 1, 2, 3, 4, 5, 6, 8]]

result = df2.reindex(midx)
expected = DataFrame({"a": [0, 1, 2, 3, 4, 5, 6, np.nan, 8]}, index=midx)
tm.assert_frame_equal(result, expected)
