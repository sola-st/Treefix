# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_libsparse.py
xindex = BlockIndex(TEST_LENGTH, xloc, xlen)
yindex = BlockIndex(TEST_LENGTH, yloc, ylen)
expected = BlockIndex(TEST_LENGTH, eloc, elen)
longer_index = BlockIndex(TEST_LENGTH + 1, yloc, ylen)

result = xindex.intersect(yindex)
assert result.equals(expected)
result = xindex.to_int_index().intersect(yindex.to_int_index())
assert result.equals(expected.to_int_index())

msg = "Indices must reference same underlying length"
with pytest.raises(Exception, match=msg):
    xindex.intersect(longer_index)
with pytest.raises(Exception, match=msg):
    xindex.to_int_index().intersect(longer_index.to_int_index())
