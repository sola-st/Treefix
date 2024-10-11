# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# https://github.com/pandas-dev/pandas/issues/16519
expected = np.empty(len(uniques), dtype=object)
expected[:] = uniques

result = pd.unique(arr)
tm.assert_numpy_array_equal(result, expected)
