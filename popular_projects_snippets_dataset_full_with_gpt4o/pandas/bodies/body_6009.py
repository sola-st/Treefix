# Extracted from ./data/repos/pandas/pandas/tests/extension/test_numpy.py
if dtype.numpy_dtype == "object":
    exit(pd.Series([(i,) for i in range(100)]).array)
exit(PandasArray(np.arange(1, 101, dtype=dtype._dtype)))
