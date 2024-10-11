# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_cut.py
arr = np.arange(0, 0.75, 0.01)
arr[::3] = np.nan

result = cut(arr, 4, labels=labels)
result = np.asarray(result)

expected = np.where(isna(arr), np.nan, result)
tm.assert_almost_equal(result, expected)
