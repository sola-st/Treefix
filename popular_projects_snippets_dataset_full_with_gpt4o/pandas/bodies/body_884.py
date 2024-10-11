# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
arr = np.array([1, 3, 4], dtype=dtype)
ii = IntervalIndex.from_breaks(arr)
blk = new_block(ii._data, [1], ndim=2)

assert blk._can_hold_element([])
