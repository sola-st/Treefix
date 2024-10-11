# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
if dtype in (np.int8, np.uint8):
    N = 100
else:
    N = 512
table = table_type()
keys = (np.arange(N) + N).astype(dtype)
table.map_locations(keys)
wrong_keys = np.arange(N).astype(dtype)
result = table.lookup(wrong_keys)
assert np.all(result == -1)
