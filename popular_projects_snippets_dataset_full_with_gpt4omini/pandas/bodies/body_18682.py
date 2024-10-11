# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
values = np.array([np.nan, np.nan, np.nan], dtype=dtype)
keys, counts = ht.value_count(values, True)
assert len(keys) == 0
keys, counts = ht.value_count(values, False)
assert len(keys) == 1 and np.all(np.isnan(keys))
assert counts[0] == 3
