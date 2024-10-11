# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_libsparse.py
xindex = BlockIndex(TEST_LENGTH, xloc, xlen)
yindex = BlockIndex(TEST_LENGTH, yloc, ylen)

# see if survive the round trip
xbindex = xindex.to_int_index().to_block_index()
ybindex = yindex.to_int_index().to_block_index()
assert isinstance(xbindex, BlockIndex)
assert xbindex.equals(xindex)
assert ybindex.equals(yindex)
