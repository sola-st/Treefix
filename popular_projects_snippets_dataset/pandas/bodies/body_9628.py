# Extracted from ./data/repos/pandas/pandas/tests/arrays/numpy_/test_numpy.py
ndarray = np.array([1, 2, 3])
ser = pd.Series(PandasArray(ndarray), copy=True)

assert ser.values is not ndarray
