# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
idx = ["a", "b", "c"]
df = DataFrame({"a": [unit, unit], "b": [unit, np.nan], "c": [np.nan, np.nan]})
# The default
result = getattr(df, method)(numeric_only=numeric_only)
expected = Series([unit, unit, unit], index=idx, dtype="float64")
tm.assert_series_equal(result, expected)

# min_count=1
result = getattr(df, method)(numeric_only=numeric_only, min_count=1)
expected = Series([unit, unit, np.nan], index=idx)
tm.assert_series_equal(result, expected)

# min_count=0
result = getattr(df, method)(numeric_only=numeric_only, min_count=0)
expected = Series([unit, unit, unit], index=idx, dtype="float64")
tm.assert_series_equal(result, expected)

result = getattr(df.iloc[1:], method)(numeric_only=numeric_only, min_count=1)
expected = Series([unit, np.nan, np.nan], index=idx)
tm.assert_series_equal(result, expected)

# min_count > 1
df = DataFrame({"A": [unit] * 10, "B": [unit] * 5 + [np.nan] * 5})
result = getattr(df, method)(numeric_only=numeric_only, min_count=5)
expected = Series(result, index=["A", "B"])
tm.assert_series_equal(result, expected)

result = getattr(df, method)(numeric_only=numeric_only, min_count=6)
expected = Series(result, index=["A", "B"])
tm.assert_series_equal(result, expected)
