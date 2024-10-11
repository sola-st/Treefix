# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_function.py
arr = pd.array(values)

res = np.add.reduce(arr)
expected = arr.sum(skipna=False)
tm.assert_almost_equal(res, expected)
