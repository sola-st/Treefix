# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
result = data_missing_for_sorting.argsort()
# argsort result gets passed to take, so should be np.intp
expected = np.array([2, 0, 1], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
