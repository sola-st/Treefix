# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
# GH#21688 ensure we can deal with readonly memory views
xs = np.array([2.718, 3.14, np.nan, -7, 5, 2, 3])
xs.setflags(write=writable)
m = ht.Float64HashTable()
m.map_locations(xs)
tm.assert_numpy_array_equal(m.lookup(xs), np.arange(len(xs), dtype=np.intp))
