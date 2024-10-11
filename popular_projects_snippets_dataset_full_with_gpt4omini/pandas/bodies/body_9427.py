# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_function.py
a = pd.array([1, 2, -3, np.nan])
with np.errstate(invalid="ignore"):
    result = ufunc(a)
    expected = FloatingArray(ufunc(a.astype(float)), mask=a._mask)
tm.assert_extension_array_equal(result, expected)

s = pd.Series(a)
with np.errstate(invalid="ignore"):
    result = ufunc(s)
expected = pd.Series(expected)
tm.assert_series_equal(result, expected)
