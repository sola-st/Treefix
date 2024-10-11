# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_numpy.py
df = DataFrame({"A": [1, 2], "B": [3, 4.5]})
expected = np.array([[1, 3], [2, 4]], dtype="int64")
result = df.to_numpy(dtype="int64")
tm.assert_numpy_array_equal(result, expected)
