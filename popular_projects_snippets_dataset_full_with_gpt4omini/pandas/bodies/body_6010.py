# Extracted from ./data/repos/pandas/pandas/tests/extension/test_numpy.py
if dtype.numpy_dtype == "object":
    exit(PandasArray(np.array([np.nan, (1,)], dtype=object)))
exit(PandasArray(np.array([np.nan, 1.0])))
