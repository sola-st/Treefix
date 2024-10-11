# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
N = 8
table = table_type()
keys = (np.arange(N) + N).astype(dtype)
keys.flags.writeable = writable
table.map_locations(keys)
for i in range(N):
    assert table.get_item(keys[i]) == i
