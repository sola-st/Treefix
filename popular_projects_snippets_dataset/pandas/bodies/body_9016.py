# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_libsparse.py
xindex = IntIndex(4, np.array([], dtype=np.int32))
yindex = IntIndex(4, np.array([2, 3], dtype=np.int32))
assert xindex.intersect(yindex).equals(xindex)
assert yindex.intersect(xindex).equals(xindex)

xindex = xindex.to_block_index()
yindex = yindex.to_block_index()
assert xindex.intersect(yindex).equals(xindex)
assert yindex.intersect(xindex).equals(xindex)
