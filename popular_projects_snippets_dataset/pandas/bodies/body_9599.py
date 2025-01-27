# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_function.py
a = pd.array([1.0, 0.2, 3.0, np.nan], dtype="Float64")
with np.errstate(invalid="ignore"):
    result = ufunc(a)
    expected = pd.array(ufunc(a.astype(float)), dtype="Float64")
tm.assert_extension_array_equal(result, expected)

s = pd.Series(a)
with np.errstate(invalid="ignore"):
    result = ufunc(s)
    expected = pd.Series(ufunc(s.astype(float)), dtype="Float64")
tm.assert_series_equal(result, expected)
