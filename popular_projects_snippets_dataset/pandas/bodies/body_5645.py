# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
arr = np.array([2**63], dtype=np.uint64)
expected = Series([1], index=[2**63])
result = algos.value_counts(arr)

tm.assert_series_equal(result, expected)

arr = np.array([-1, 2**63], dtype=object)
expected = Series([1, 1], index=[-1, 2**63])
result = algos.value_counts(arr)

tm.assert_series_equal(result, expected)
