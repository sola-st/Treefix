# Extracted from ./data/repos/pandas/pandas/tests/arrays/numpy_/test_numpy.py
arr = np.array([0, 1])
result = PandasArray(arr, copy=True)

assert not tm.shares_memory(result, arr)
