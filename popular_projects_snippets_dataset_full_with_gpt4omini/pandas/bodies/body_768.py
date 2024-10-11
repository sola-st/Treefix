# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_missing.py
# scalars GH#23530
a = Decimal(1.0)
assert isna(a) is False
assert notna(a) is True

b = Decimal("NaN")
assert isna(b) is True
assert notna(b) is False

# array
arr = np.array([a, b])
expected = np.array([False, True])
result = isna(arr)
tm.assert_numpy_array_equal(result, expected)

result = notna(arr)
tm.assert_numpy_array_equal(result, ~expected)

# series
ser = Series(arr)
expected = Series(expected)
result = isna(ser)
tm.assert_series_equal(result, expected)

result = notna(ser)
tm.assert_series_equal(result, ~expected)

# index
idx = Index(arr)
expected = np.array([False, True])
result = isna(idx)
tm.assert_numpy_array_equal(result, expected)

result = notna(idx)
tm.assert_numpy_array_equal(result, ~expected)
