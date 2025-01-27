# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
table = ht.PyObjectHashTable()
keys = np.array([complex(float("nan"), 1.0) for i in range(50)], dtype=np.object_)
unique = table.unique(keys)
assert len(unique) == 1
