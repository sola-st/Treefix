# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_quantile.py
# GH#42849
df = DataFrame({"x": [1, 1], "y": [pd.NA] * 2}, dtype=dtype)
result = df.groupby("x")["y"].quantile(0.5)
expected = pd.Series(
    [np.nan], dtype=dtype, index=Index([1.0], dtype=dtype), name="y"
)
expected.index.name = "x"
tm.assert_series_equal(expected, result)
