# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_util.py
x, y = list("ABC"), [1, 22]
result1, result2 = cartesian_product([x, y])
expected1 = np.array(["A", "A", "B", "B", "C", "C"])
expected2 = np.array([1, 22, 1, 22, 1, 22])
tm.assert_numpy_array_equal(result1, expected1)
tm.assert_numpy_array_equal(result2, expected2)
