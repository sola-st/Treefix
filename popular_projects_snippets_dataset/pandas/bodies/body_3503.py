# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_quantile.py
# GH 14564
df = DataFrame(columns=["a", "b"], dtype=dtype)
result = df.quantile(0.5, axis=axis, numeric_only=False)
expected = Series(
    expected_data, name=0.5, index=Index(expected_index), dtype=expected_dtype
)
tm.assert_series_equal(result, expected)
