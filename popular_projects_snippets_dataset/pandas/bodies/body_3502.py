# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_quantile.py
# GH 14564
df = DataFrame(columns=["a", "b"], dtype=dtype)
result = df.quantile(0.5, axis=axis)
expected = Series(
    expected_data, name=0.5, index=Index(expected_index), dtype="float64"
)
tm.assert_series_equal(result, expected)
