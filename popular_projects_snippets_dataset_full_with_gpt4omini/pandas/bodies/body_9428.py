# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_function.py
# two IntegerArrays
a = pd.array([1, 2, -3, np.nan])
result = ufunc(a, a)
expected = pd.array(ufunc(a.astype(float), a.astype(float)), dtype="Int64")
tm.assert_extension_array_equal(result, expected)

# IntegerArray with numpy array
arr = np.array([1, 2, 3, 4])
result = ufunc(a, arr)
expected = pd.array(ufunc(a.astype(float), arr), dtype="Int64")
tm.assert_extension_array_equal(result, expected)

result = ufunc(arr, a)
expected = pd.array(ufunc(arr, a.astype(float)), dtype="Int64")
tm.assert_extension_array_equal(result, expected)

# IntegerArray with scalar
result = ufunc(a, 1)
expected = pd.array(ufunc(a.astype(float), 1), dtype="Int64")
tm.assert_extension_array_equal(result, expected)

result = ufunc(1, a)
expected = pd.array(ufunc(1, a.astype(float)), dtype="Int64")
tm.assert_extension_array_equal(result, expected)
