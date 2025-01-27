# Extracted from ./data/repos/pandas/pandas/tests/arrays/numpy_/test_numpy.py
arr = PandasArray(np.array([-1.0, 0.0, 1.0]))
result = ufunc(arr)
expected = PandasArray(ufunc(arr._ndarray))
tm.assert_extension_array_equal(result, expected)

# same thing but with the 'out' keyword
out = PandasArray(np.array([-9.0, -9.0, -9.0]))
ufunc(arr, out=out)
tm.assert_extension_array_equal(out, expected)
