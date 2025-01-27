# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# GH#47105
idx = Index([np.nan])
expected = np.array([False])

result = op(idx, idx)
tm.assert_numpy_array_equal(result, expected)

result = op(idx, idx.copy())
tm.assert_numpy_array_equal(result, expected)
