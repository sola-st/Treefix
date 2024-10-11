# Extracted from ./data/repos/pandas/pandas/tests/extension/test_common.py

arr = DummyArray(np.array([1, 2, 3]))
expected = np.array([1, 2, 3], dtype=object)

result = arr.astype(object)
tm.assert_numpy_array_equal(result, expected)

result = arr.astype("object")
tm.assert_numpy_array_equal(result, expected)
