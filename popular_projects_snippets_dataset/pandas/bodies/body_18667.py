# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
N = 10
table = table_type()
keys = np.full(N, np.nan, dtype=dtype)
table.map_locations(keys)
assert len(table) == 1
assert table.get_item(np.nan) == N - 1
