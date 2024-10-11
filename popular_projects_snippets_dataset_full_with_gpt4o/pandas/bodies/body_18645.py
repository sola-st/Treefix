# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
with activated_tracemalloc():
    table = table_type()
    used = get_allocated_khash_memory()
    my_size = table.sizeof()
    assert used == my_size
    del table
    assert get_allocated_khash_memory() == 0
