# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
if table_type == ht.PyObjectHashTable:
    pytest.skip("Mask not supported for object")
N = 3
table = table_type(uses_mask=True)
keys = (np.arange(N) + N).astype(dtype)
mask = np.array([False, True, False])
keys.flags.writeable = writable
table.map_locations(keys, mask)
result = table.lookup(keys, mask)
expected = np.arange(N)
tm.assert_numpy_array_equal(result.astype(np.int64), expected.astype(np.int64))

result = table.lookup(np.array([1 + N]).astype(dtype), np.array([False]))
tm.assert_numpy_array_equal(
    result.astype(np.int64), np.array([-1], dtype=np.int64)
)
