# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_quantile.py
df = DataFrame({"a": [1], "b": [2.0], "c": ["x"]})
if numeric_only:
    result = df.groupby("a").quantile(q, numeric_only=numeric_only)
    expected = df.groupby("a")[["b"]].quantile(q)
    tm.assert_frame_equal(result, expected)
else:
    with pytest.raises(
        TypeError, match="'quantile' cannot be performed against 'object' dtypes!"
    ):
        df.groupby("a").quantile(q, numeric_only=numeric_only)
