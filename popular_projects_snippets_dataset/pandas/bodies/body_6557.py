# Extracted from ./data/repos/pandas/pandas/tests/test_take.py
result = algos.take(np.array([]), [-1, -1], allow_fill=True, fill_value=0.0)
expected = np.array([0.0, 0.0])
tm.assert_numpy_array_equal(result, expected)
