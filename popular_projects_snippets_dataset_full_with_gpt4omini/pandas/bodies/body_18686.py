# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
values = np.array([42, np.nan, np.nan, np.nan], dtype=dtype)
assert ht.mode(values, True) == 42
assert np.isnan(ht.mode(values, False))
