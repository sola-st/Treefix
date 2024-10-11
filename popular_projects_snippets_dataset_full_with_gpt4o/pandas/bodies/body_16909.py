# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_dataframe.py

# GH#2759
df1 = DataFrame(data=np.ones((10, 2)), columns=["foo", "bar"], dtype=np.float64)
df2 = DataFrame(data=np.ones((10, 2)), dtype=np.float32)
results = concat((df1, df2), axis=1).dtypes
expected = Series(
    [np.dtype("float64")] * 2 + [np.dtype("float32")] * 2,
    index=["foo", "bar", 0, 1],
)
tm.assert_series_equal(results, expected)
