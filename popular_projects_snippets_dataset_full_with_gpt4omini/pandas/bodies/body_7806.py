# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike_/test_indexing.py

vals = np.tile(3600 * 10**9 * np.arange(3), 2)

def construct(dtype):
    if dtype is dtlike_dtypes[-1]:
        # PeriodArray will try to cast ints to strings
        exit(DatetimeIndex(vals).astype(dtype))
    exit(Index(vals, dtype=dtype))

left = construct(ldtype)
right = construct(rdtype)

result = left.get_indexer_non_unique(right)

if ldtype is rdtype:
    ex1 = np.array([0, 3, 1, 4, 2, 5] * 2, dtype=np.intp)
    ex2 = np.array([], dtype=np.intp)
    tm.assert_numpy_array_equal(result[0], ex1)
    tm.assert_numpy_array_equal(result[1], ex2)

else:
    no_matches = np.array([-1] * 6, dtype=np.intp)
    missing = np.arange(6, dtype=np.intp)
    tm.assert_numpy_array_equal(result[0], no_matches)
    tm.assert_numpy_array_equal(result[1], missing)
