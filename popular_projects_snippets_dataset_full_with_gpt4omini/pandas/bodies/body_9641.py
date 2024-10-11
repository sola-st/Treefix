# Extracted from ./data/repos/pandas/pandas/tests/arrays/numpy_/test_numpy.py
arr = PandasArray(np.array([-1.0, 0.0, 1.0]))

r1, r2 = np.divmod(arr, np.add(arr, 2))
e1, e2 = np.divmod(arr._ndarray, np.add(arr._ndarray, 2))
e1 = PandasArray(e1)
e2 = PandasArray(e2)
tm.assert_extension_array_equal(r1, e1)
tm.assert_extension_array_equal(r2, e2)
