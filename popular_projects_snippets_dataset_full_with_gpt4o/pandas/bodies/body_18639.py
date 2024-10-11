# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
if table_type == ht.PyObjectHashTable:
    pytest.skip("Mask not supported for object")
N = 3
table = table_type(uses_mask=True)
keys = (np.arange(N) + N).astype(dtype)
keys.flags.writeable = writable
table.map_locations(keys, np.array([False, False, True]))
for i in range(N - 1):
    assert table.get_item(keys[i]) == i

with pytest.raises(KeyError, match=re.escape(str(keys[N - 1]))):
    table.get_item(keys[N - 1])

assert table.get_na() == 2
