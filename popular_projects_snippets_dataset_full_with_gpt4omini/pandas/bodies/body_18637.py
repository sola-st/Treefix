# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
# only Int64HashTable has this method
if table_type == ht.Int64HashTable:
    N = 77
    table = table_type()
    keys = np.arange(N).astype(dtype)
    vals = np.arange(N).astype(np.int64) + N
    keys.flags.writeable = writable
    vals.flags.writeable = writable
    table.map_keys_to_values(keys, vals)
    for i in range(N):
        assert table.get_item(keys[i]) == i + N
