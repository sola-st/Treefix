# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_function.py
# two FloatingArrays
a = pd.array([1, 0.2, -3, np.nan], dtype="Float64")
result = ufunc(a, a)
expected = pd.array(ufunc(a.astype(float), a.astype(float)), dtype="Float64")
tm.assert_extension_array_equal(result, expected)

# FloatingArray with numpy array
arr = np.array([1, 2, 3, 4])
result = ufunc(a, arr)
expected = pd.array(ufunc(a.astype(float), arr), dtype="Float64")
tm.assert_extension_array_equal(result, expected)

result = ufunc(arr, a)
expected = pd.array(ufunc(arr, a.astype(float)), dtype="Float64")
tm.assert_extension_array_equal(result, expected)

# FloatingArray with scalar
result = ufunc(a, 1)
expected = pd.array(ufunc(a.astype(float), 1), dtype="Float64")
tm.assert_extension_array_equal(result, expected)

result = ufunc(1, a)
expected = pd.array(ufunc(1, a.astype(float)), dtype="Float64")
tm.assert_extension_array_equal(result, expected)
