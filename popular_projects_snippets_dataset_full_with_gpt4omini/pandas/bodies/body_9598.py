# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_function.py
a = pd.array([1, 2, -3, np.nan], dtype="Float64")
result = ufunc(a)
expected = pd.array(ufunc(a.astype(float)), dtype="Float64")
tm.assert_extension_array_equal(result, expected)

s = pd.Series(a)
result = ufunc(s)
expected = pd.Series(expected)
tm.assert_series_equal(result, expected)
