# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
N = 1000
keys = np.arange(N).astype(np.compat.unicode).astype(np.object_)
with activated_tracemalloc():
    table = ht.StringHashTable()
    table.map_locations(keys)
    used = get_allocated_khash_memory()
    my_size = table.sizeof()
    assert used == my_size
    del table
    assert get_allocated_khash_memory() == 0
