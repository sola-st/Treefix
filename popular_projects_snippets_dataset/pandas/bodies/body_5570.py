# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# nan should map to na_sentinel, not reverse_indexer[na_sentinel]
# rizer.factorize should not raise an exception if na_sentinel indexes
# outside of reverse_indexer
key = np.array([1, 2, 1, np.nan], dtype="O")
rizer = ht.ObjectFactorizer(len(key))
for na_sentinel in (-1, 20):
    ids = rizer.factorize(key, na_sentinel=na_sentinel)
    expected = np.array([0, 1, 0, na_sentinel], dtype=np.intp)
    assert len(set(key)) == len(set(expected))
    tm.assert_numpy_array_equal(pd.isna(key), expected == na_sentinel)
    tm.assert_numpy_array_equal(ids, expected)
