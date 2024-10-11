# Extracted from ./data/repos/pandas/pandas/tests/arrays/numpy_/test_numpy.py
nparr = any_numpy_array
arr = PandasArray(nparr, copy=True)

arr[0] = arr[1]
nparr[0] = nparr[1]

tm.assert_numpy_array_equal(arr.to_numpy(), nparr)
