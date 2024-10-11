# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_cut.py
arr = np.random.randn(100)
result = cut(arr, [-1, 0, 1])

mask = isna(result)
ex_mask = (arr < -1) | (arr > 1)
tm.assert_numpy_array_equal(mask, ex_mask)
