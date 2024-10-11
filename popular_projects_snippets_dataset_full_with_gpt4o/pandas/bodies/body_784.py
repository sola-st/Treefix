# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_missing.py
result = libmissing.isnaobj(arr)
tm.assert_numpy_array_equal(result, expected)
result = libmissing.isnaobj(arr, inf_as_na=True)
tm.assert_numpy_array_equal(result, expected)

arr = np.atleast_2d(arr)
expected = np.atleast_2d(expected)

result = libmissing.isnaobj(arr)
tm.assert_numpy_array_equal(result, expected)
result = libmissing.isnaobj(arr, inf_as_na=True)
tm.assert_numpy_array_equal(result, expected)

# Test fortran order
arr = arr.copy(order="F")
result = libmissing.isnaobj(arr)
tm.assert_numpy_array_equal(result, expected)
result = libmissing.isnaobj(arr, inf_as_na=True)
tm.assert_numpy_array_equal(result, expected)
