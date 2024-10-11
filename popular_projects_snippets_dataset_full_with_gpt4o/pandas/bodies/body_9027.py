# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_libsparse.py
locs = [0, 10]
lengths = [4, 6]
exp_inds = [0, 1, 2, 3, 10, 11, 12, 13, 14, 15]

block = BlockIndex(20, locs, lengths)
dense = block.to_int_index()

tm.assert_numpy_array_equal(dense.indices, np.array(exp_inds, dtype=np.int32))
