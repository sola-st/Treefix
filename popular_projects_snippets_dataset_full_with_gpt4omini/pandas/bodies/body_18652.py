# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
xs = np.array([1, 2, 2**63], dtype=np.uint64)
# GH 21688 ensure we can deal with readonly memory views
xs.setflags(write=writable)
m = ht.UInt64HashTable()
m.map_locations(xs)
tm.assert_numpy_array_equal(m.lookup(xs), np.arange(len(xs), dtype=np.intp))
