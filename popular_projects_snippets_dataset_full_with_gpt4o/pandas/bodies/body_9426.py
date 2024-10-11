# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_function.py
a = pd.array([1, 2, -3, np.nan])
result = ufunc(a)
expected = pd.array(ufunc(a.astype(float)), dtype="Int64")
tm.assert_extension_array_equal(result, expected)

s = pd.Series(a)
result = ufunc(s)
expected = pd.Series(pd.array(ufunc(a.astype(float)), dtype="Int64"))
tm.assert_series_equal(result, expected)
