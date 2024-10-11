# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
N = 1020
table = table_type()
keys = np.full(N, np.nan, dtype=dtype)
unique = table.unique(keys)
assert np.all(np.isnan(unique)) and len(unique) == 1
