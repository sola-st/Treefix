# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py

mindex = MultiIndex.from_arrays(
    [np.arange(5).repeat(5), np.tile(np.arange(5), 5)]
)
expected = mindex.values
expected.sort()

mindex = mindex.repeat(2)

result = pd.unique(mindex)
result.sort()

tm.assert_almost_equal(result, expected)
