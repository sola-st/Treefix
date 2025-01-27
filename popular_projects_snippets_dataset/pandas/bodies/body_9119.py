# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_sorting.py
c = Categorical([5, 3, 1, 4, 2], ordered=True)

expected = np.array([2, 4, 1, 3, 0])
tm.assert_numpy_array_equal(
    c.argsort(ascending=True), expected, check_dtype=False
)

expected = expected[::-1]
tm.assert_numpy_array_equal(
    c.argsort(ascending=False), expected, check_dtype=False
)
