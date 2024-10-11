# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py

# doc example reshaping.rst
x = Series(["A", "A", np.nan, "B", 3.14, np.inf])
codes, uniques = algos.factorize(x)

exp = np.array([0, 0, -1, 1, 2, 3], dtype=np.intp)
tm.assert_numpy_array_equal(codes, exp)
exp = Index(["A", "B", 3.14, np.inf])
tm.assert_index_equal(uniques, exp)

codes, uniques = algos.factorize(x, sort=True)
exp = np.array([2, 2, -1, 3, 0, 1], dtype=np.intp)
tm.assert_numpy_array_equal(codes, exp)
exp = Index([3.14, np.inf, "A", "B"])
tm.assert_index_equal(uniques, exp)
