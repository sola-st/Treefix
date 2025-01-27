# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_function.py
arr = pd.array(values, dtype="Float64")

res = np.add.reduce(arr)
expected = arr.sum(skipna=False)
tm.assert_almost_equal(res, expected)
