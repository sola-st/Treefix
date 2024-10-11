# Extracted from ./data/repos/pandas/pandas/tests/arrays/numpy_/test_numpy.py
ndarray = np.array([1, 2, 3])
result = pd.Series(PandasArray(ndarray), dtype="float64")
expected = pd.Series([1.0, 2.0, 3.0], dtype="float64")
tm.assert_series_equal(result, expected)
