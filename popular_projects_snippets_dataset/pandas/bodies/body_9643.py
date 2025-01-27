# Extracted from ./data/repos/pandas/pandas/tests/arrays/numpy_/test_numpy.py
arr = PandasArray(np.array(["a", "b", "c"], dtype=dtype))
arr[0] = "t"
expected = PandasArray(np.array(["t", "b", "c"], dtype=dtype))
tm.assert_extension_array_equal(arr, expected)
