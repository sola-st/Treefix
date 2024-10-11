# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
keys = np.array([0, 1, np.nan, 0, 2, np.nan], dtype=object)

result = algos.duplicated(keys)
expected = np.array([False, False, False, True, False, True])
tm.assert_numpy_array_equal(result, expected)

result = algos.duplicated(keys, keep="first")
expected = np.array([False, False, False, True, False, True])
tm.assert_numpy_array_equal(result, expected)

result = algos.duplicated(keys, keep="last")
expected = np.array([True, False, True, False, False, False])
tm.assert_numpy_array_equal(result, expected)

result = algos.duplicated(keys, keep=False)
expected = np.array([True, False, True, True, False, True])
tm.assert_numpy_array_equal(result, expected)

keys = np.empty(8, dtype=object)
for i, t in enumerate(
    zip([0, 0, np.nan, np.nan] * 2, [0, np.nan, 0, np.nan] * 2)
):
    keys[i] = t

result = algos.duplicated(keys)
falses = [False] * 4
trues = [True] * 4
expected = np.array(falses + trues)
tm.assert_numpy_array_equal(result, expected)

result = algos.duplicated(keys, keep="last")
expected = np.array(trues + falses)
tm.assert_numpy_array_equal(result, expected)

result = algos.duplicated(keys, keep=False)
expected = np.array(trues + trues)
tm.assert_numpy_array_equal(result, expected)
