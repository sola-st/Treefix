# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_unique.py
# decision about None
ser = Series([1, 2, 3, None, None, None], dtype=object)
result = ser.unique()
expected = np.array([1, 2, 3, None], dtype=object)
tm.assert_numpy_array_equal(result, expected)
