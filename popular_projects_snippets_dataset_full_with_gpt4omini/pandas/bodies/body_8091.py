# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
index = Index(values)
result = index == values
expected = np.array([True, True, True, True], dtype=bool)

tm.assert_numpy_array_equal(result, expected)
