# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# GH12558
s = Series([1] * 2 + [2] * 3 + [np.nan] * 5)
s_typed = s.astype(dtype)
result = s_typed.value_counts(normalize=True, dropna=False)
expected = Series(
    [0.5, 0.3, 0.2], index=Series([np.nan, 2.0, 1.0], dtype=dtype)
)
tm.assert_series_equal(result, expected)

result = s_typed.value_counts(normalize=True, dropna=True)
expected = Series([0.6, 0.4], index=Series([2.0, 1.0], dtype=dtype))
tm.assert_series_equal(result, expected)
