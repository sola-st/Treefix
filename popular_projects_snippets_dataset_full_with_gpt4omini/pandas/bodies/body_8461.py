# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_misc.py
dti = DatetimeIndex(np.arange(10))
expected = Index(np.arange(10, dtype=np.int32))

tm.assert_index_equal(dti.nanosecond, expected)
