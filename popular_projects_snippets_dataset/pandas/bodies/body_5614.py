# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py

result = algos.isin([1, 2], [1])
expected = np.array([True, False])
tm.assert_numpy_array_equal(result, expected)

result = algos.isin(np.array([1, 2]), [1])
expected = np.array([True, False])
tm.assert_numpy_array_equal(result, expected)

result = algos.isin(Series([1, 2]), [1])
expected = np.array([True, False])
tm.assert_numpy_array_equal(result, expected)

result = algos.isin(Series([1, 2]), Series([1]))
expected = np.array([True, False])
tm.assert_numpy_array_equal(result, expected)

result = algos.isin(Series([1, 2]), {1})
expected = np.array([True, False])
tm.assert_numpy_array_equal(result, expected)

result = algos.isin(["a", "b"], ["a"])
expected = np.array([True, False])
tm.assert_numpy_array_equal(result, expected)

result = algos.isin(Series(["a", "b"]), Series(["a"]))
expected = np.array([True, False])
tm.assert_numpy_array_equal(result, expected)

result = algos.isin(Series(["a", "b"]), {"a"})
expected = np.array([True, False])
tm.assert_numpy_array_equal(result, expected)

result = algos.isin(["a", "b"], [1])
expected = np.array([False, False])
tm.assert_numpy_array_equal(result, expected)
