# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py

codes, uniques = algos.factorize(["a", "b", "b", "a", "a", "c", "c", "c"])
tm.assert_numpy_array_equal(uniques, np.array(["a", "b", "c"], dtype=object))

codes, uniques = algos.factorize(
    ["a", "b", "b", "a", "a", "c", "c", "c"], sort=True
)
exp = np.array([0, 1, 1, 0, 0, 2, 2, 2], dtype=np.intp)
tm.assert_numpy_array_equal(codes, exp)
exp = np.array(["a", "b", "c"], dtype=object)
tm.assert_numpy_array_equal(uniques, exp)

arr = np.arange(5, dtype=np.intp)[::-1]

codes, uniques = algos.factorize(arr)
exp = np.array([0, 1, 2, 3, 4], dtype=np.intp)
tm.assert_numpy_array_equal(codes, exp)
exp = np.array([4, 3, 2, 1, 0], dtype=arr.dtype)
tm.assert_numpy_array_equal(uniques, exp)

codes, uniques = algos.factorize(arr, sort=True)
exp = np.array([4, 3, 2, 1, 0], dtype=np.intp)
tm.assert_numpy_array_equal(codes, exp)
exp = np.array([0, 1, 2, 3, 4], dtype=arr.dtype)
tm.assert_numpy_array_equal(uniques, exp)

arr = np.arange(5.0)[::-1]

codes, uniques = algos.factorize(arr)
exp = np.array([0, 1, 2, 3, 4], dtype=np.intp)
tm.assert_numpy_array_equal(codes, exp)
exp = np.array([4.0, 3.0, 2.0, 1.0, 0.0], dtype=arr.dtype)
tm.assert_numpy_array_equal(uniques, exp)

codes, uniques = algos.factorize(arr, sort=True)
exp = np.array([4, 3, 2, 1, 0], dtype=np.intp)
tm.assert_numpy_array_equal(codes, exp)
exp = np.array([0.0, 1.0, 2.0, 3.0, 4.0], dtype=arr.dtype)
tm.assert_numpy_array_equal(uniques, exp)
