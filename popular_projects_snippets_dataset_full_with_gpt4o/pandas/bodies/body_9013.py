# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_libsparse.py
# Case 1
# x: ----
# y:     ----
# r: --------
# Case 2
# x: -----     -----
# y:   -----          --
# Case 3
# x: ------
# y:    -------
# r: ----------
# Case 4
# x: ------  -----
# y:    -------
# r: -------------
# Case 5
# x: ---  -----
# y: -------
# r: -------------
# Case 6
# x: ------  -----
# y:    -------  ---
# r: -------------
# Case 7
# x: ----------------------
# y:   ----  ----   ---
# r: ----------------------
# Case 8
# x: ----       ---
# y:       ---       ---
xindex = BlockIndex(TEST_LENGTH, xloc, xlen)
yindex = BlockIndex(TEST_LENGTH, yloc, ylen)
bresult = xindex.make_union(yindex)
assert isinstance(bresult, BlockIndex)
tm.assert_numpy_array_equal(bresult.blocs, np.array(eloc, dtype=np.int32))
tm.assert_numpy_array_equal(bresult.blengths, np.array(elen, dtype=np.int32))

ixindex = xindex.to_int_index()
iyindex = yindex.to_int_index()
iresult = ixindex.make_union(iyindex)
assert isinstance(iresult, IntIndex)
tm.assert_numpy_array_equal(iresult.indices, bresult.to_int_index().indices)
