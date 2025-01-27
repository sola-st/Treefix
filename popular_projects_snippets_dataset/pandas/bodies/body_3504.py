# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_quantile.py
# GH 14564
df = DataFrame(
    {
        "a": pd.to_datetime(["2010", "2011"]),
        "b": [0, 5],
        "c": pd.to_datetime(["2011", "2012"]),
    }
)
result = df[["a", "c"]].quantile(0.5, axis=axis, numeric_only=True)
expected = Series(
    expected_data, name=0.5, index=Index(expected_index), dtype=np.float64
)
tm.assert_series_equal(result, expected)
