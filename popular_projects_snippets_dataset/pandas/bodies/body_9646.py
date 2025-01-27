# Extracted from ./data/repos/pandas/pandas/tests/arrays/numpy_/test_numpy.py
# we should get back np.nans, not -1s
arr = PandasArray(np.array([], dtype=dtype))
idx = pd.Index([0.0, 0.5])

result = arr._quantile(idx, interpolation="linear")
expected = PandasArray(np.array([np.nan, np.nan]))
tm.assert_extension_array_equal(result, expected)
