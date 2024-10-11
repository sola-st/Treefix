# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_to_numpy.py
# GH#50600
ser = Series([1])
result = ser.to_numpy(dtype=np.float64, na_value=np.nan)
expected = np.array([1.0])
tm.assert_numpy_array_equal(result, expected)
