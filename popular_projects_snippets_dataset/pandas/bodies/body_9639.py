# Extracted from ./data/repos/pandas/pandas/tests/arrays/numpy_/test_numpy.py
raw = np.arange(12).reshape(4, 3)
arr = PandasArray(raw)

res = np.maximum.reduce(arr, axis=0)
tm.assert_extension_array_equal(res, arr[-1])

alt = arr.max(axis=0)
tm.assert_extension_array_equal(alt, arr[-1])
