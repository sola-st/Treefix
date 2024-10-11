# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
if dtype in (np.int8, np.uint8):
    N = 256
else:
    N = 30000
keys = np.arange(N).astype(dtype)
with activated_tracemalloc():
    table = table_type()
    table.map_locations(keys)
    used = get_allocated_khash_memory()
    my_size = table.sizeof()
    assert used == my_size
    del table
    assert get_allocated_khash_memory() == 0
